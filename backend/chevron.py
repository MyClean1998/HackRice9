import random
import pandas as pd
from workScheduling import WorkSchedulingState
from qlearningAgent import QLearningAgent
import copy


class Chevron:
    def __init__(self, sess, equipment_file, facility_file, worker_file, workOrder_file, is_training=False):
        self.equip_failure_prob = {}
        self.equip_fixing_time = {}

        self.fac_loc = {}
        self.fac_equip_info = {}

        self.workOrder_id = 1
        self.agent = QLearningAgent(0.9, 0.1, 0.1, 1000, sess, is_training)
        
        self.equipment_file = equipment_file
        self.facility_file = facility_file
        self.worker_file = worker_file
        self.workOrder_file = workOrder_file
        
    
    def __str__(self):
        return str(self.work_state)
    
    def initialize(self):
        self.load_facility_equipment_info(self.equipment_file, self.facility_file)
        facilities = self.initialize_facility()
        workers = self.initialize_workers(self.worker_file)
        work_orders = self.initialize_work_orders(self.workOrder_file, 0)
        self.work_state = WorkSchedulingState(workers, facilities, work_orders)
        self.work_state.generate_action()
        self.agent.set_evoke_func(lambda action: self.update_work_state(action))


    def load_facility_equipment_info(self, equipment_file, facility_file):
        equipment_df = pd.read_csv(equipment_file, header=1).iloc[:, 1:]
        facility_df = pd.read_csv(facility_file, header=1).iloc[:, 1:]

        for idx, row in equipment_df.iterrows():
            name = row["Equipment"]
            failureProb = float(row["Probability of Failure"])
            fixingTime = list(map(lambda x: int(x), row["Hours to Fix (range)"].split("-")))
            self.equip_failure_prob[name] = failureProb
            self.equip_fixing_time[name] = fixingTime

        for idx, row in facility_df.iterrows():
            fac_name = row["Facility"]
            location = (float(row["Latitude"]), float(row["Longitude"]))
            self.fac_loc[fac_name] = location
            fac_equip = {}
            fac_equip_df = equipment_df[["Equipment", fac_name]]
            for idx, row in fac_equip_df.iterrows():
                fac_equip[row["Equipment"]] = int(row[fac_name])
            self.fac_equip_info[fac_name] = fac_equip

    def initialize_facility(self):
        facilities = []
        for fac in self.fac_loc.keys():
            facility = Facility(fac, self.fac_loc[fac], self.fac_equip_info[fac], self.equip_failure_prob, self.equip_fixing_time)
            facilities.append(facility)
        return facilities

    def initialize_workers(self, worker_file):
        workers = []
        worker_df = pd.read_csv(worker_file).iloc[:, 1:]
        for idx, row in worker_df.iterrows():
            name = row["Name"]
            certification = row["Equipment Certification(s)"]
            shift = row["Shifts"]
            worker = Worker(name, certification, shift)
            workers.append(worker)
        return workers
    
    def initialize_work_orders(self, workOrder_file, start_time):
        work_orders = []
        workOrder_df = pd.read_csv(workOrder_file, header=1).iloc[:, 1:]
        for idx, row in workOrder_df.iterrows():
            equipment = row["Equipment Type"]
            priority = row["Priority(1-5)"]
            duration = row["Time to Complete"]
            submission_time = start_time
            work_order = WorkOrder(self.workOrder_id, equipment, priority, duration, submission_time)
            self.workOrder_id += 1
            work_orders.append(work_order)
        return work_orders

    def update_work_state(self, action):
        self.agent.do_action(self.work_state)
    
    def one_timestep_passed(self):
        state_changed = False

        jobs = self.work_state.get_jobs(job_status="in progress")
        for job in jobs:
            if job.one_timestep_passed():
                state_changed = True
                self.work_state.delete_jobs(job.id)
        
        facilities = self.work_state.get_facilities()
        for fac in facilities:
            state_changed = state_changed or fac.one_timestep_passed()

        workers = self.work_state.get_workers()
        for worker in workers:
            state_changed = state_changed or worker.one_timestep_passed()
        
        self.agent.do_action(self.work_state)



class Equipment:
    def __init__(self, name, id, prob_failure, fixing_time, status=0):
        self.name = name
        self.prob_failure = prob_failure
        self.fixing_time = fixing_time
        self.status = status

    def get_fixing_time(self):
        return random.randint(*self.fixing_time)
        
    def is_available(self):
        return self.status == 0

    def put_towork(self, hours):
        self.status = hours
    
    def one_timestep_passed(self):
        # Return whether current equipment is finished
        if not self.is_available:
            self.status -= 1
            if self.status == 0:
                return True
        return False


class Facility:
    def __init__(self, name, position, num_equipments, equip_failure_prob, equip_fixing_time):
        self.name = name
        self.position = position
        self.num_equipments = num_equipments
        self.equipments = {}
        self.initialize_equipments(equip_failure_prob, equip_fixing_time)

    def initialize_equipments(self, equip_failure_prob, equip_fixing_time):
        for equip_name in self.num_equipments:
            num_equipment = self.num_equipments[equip_name]
            self.equipments[equip_name] = [Equipment(equip_name, i, equip_failure_prob[equip_name], equip_fixing_time[equip_name]) for i in range(num_equipment)]

    def get_all_equipments(self):
        all_equips = []
        for equip in self.equipments.values():
            all_equips += equip
        return all_equips

    def has_available_equipment(self, equip_name):
        for equip in self.equipments[equip_name]:
            if equip.is_available():
                return True
        return False

    def put_equipment_towork(self, equip_name, hours):
        for equip in self.equipments[equip_name]:
            if equip.is_available():
                equip.put_towork(hours)
    
    def one_timestep_passed(self):
        state_changed = False
        equipments = self.get_all_equipments()
        for equip in equipments:
            state_changed = state_changed or equip.one_timestep_passed()
        return state_changed


class Worker:
    def __init__(self, name, certification, shift, status=0):
        self.name = name
        self.certification = certification
        self.shift = shift
        self.status = status

    def change_status(self, new_status):
        self.status = new_status
    
    def is_available(self):
        return self.status == 0

    def put_towork(self, hours):
        self.status = hours
    
    def one_timestep_passed(self):
        # Return whether current worker is done his job
        if not self.is_available:
            self.status -= 1
            if self.status == 0:
                return True
        return False
    

class WorkOrder:
    def __init__(self, id, equipment, priority, duration, submission_time, time_waited=0, status="pending"):
        self.id = id
        self.equipment = equipment
        self.priority = priority
        self.duration = duration
        self.submission_time = submission_time
        self.time_waited = time_waited
        self.status = status
        self.time_rest = duration
    
    def __str__(self):
        return "[jobid: {}; status: {}; equipment: {}; priority: {}; time_rest: {}; time_waited: {}; submission_time: {}".format(self.id, self.status, self.equipment, self.priority, self.time_rest, self.time_waited, self.submission_time)
    
    def is_pending(self):
        return self.status == "pending"
    
    def is_in_progress(self):
        return self.status == "in progress"

    def put_pending(self):
        self.status = "pending"

    def put_in_progress(self):
        self.status = "in progress"
    
    def one_timestep_passed(self):
        # Return whether current work order is finished
        if self.is_in_progress():
            self.time_rest = 1
            if self.time_rest == 0:
                return True
        elif self.is_pending():
            self.time_waited += 1
        return False
        
    
    

if __name__ == '__main__':
    chevron = Chevron("equipment.csv", "facility.csv", "worker.csv", "workOrder.csv")
    # chevron2 = copy.deepcopy(chevron)
    # chevron2.work_state.workers[0].put_towork(2)
    # print(chevron2.work_state.workers[0].name, chevron2.work_state.workers[0].is_available())
    # print(chevron2.work_state.workers[0].name, chevron.work_state.workers[0].is_available())

