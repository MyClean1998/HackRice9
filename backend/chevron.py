import random
import pandas as pd
from workScheduling import WorkSchedulingState
from qlearningAgent import QLearningAgent
import copy
import numpy as np


class Chevron:
    def __init__(self, agent, equipment_file, facility_file, worker_file, workOrder_file, is_training=False):

        self.fac_info = []
        self.equip_info = {}
        self.equips = {}
        self.workers = []
        self.work_orders = []

        self.workOrder_id = 1
        self.agent = agent
        self.equipment_names = ['Pump', 'Compressor', 'Seperator', 'Sensor', 'Security', 'Electricity', 'Networking', 'Vehicle', 'HVAC', 'Conveyer']
        
        self.equipment_file = equipment_file
        self.facility_file = facility_file
        self.worker_file = worker_file
        self.workOrder_file = workOrder_file
        self.time_step = 0
        
    
    def __str__(self):
        return str(self.work_state)
    
    def initialize(self):
        self.load_facility_equipment_info(self.equipment_file, self.facility_file)
        self.initialize_workers(self.worker_file)
        self.initialize_work_orders(self.workOrder_file, 0)
        self.work_state = WorkSchedulingState(self.workers, self.equips, self.work_orders, self.equip_info, self.fac_info)
        self.agent.set_evoke_func(lambda action: self.update_work_state())

    def load_facility_equipment_info(self, equipment_file, facility_file):
        equipment_df = pd.read_csv(equipment_file, header=1).iloc[:, 1:]
        facility_df = pd.read_csv(facility_file, header=1).iloc[:, 1:]

        fac_num, _ = facility_df.shape
        equip_type_num, _ = equipment_df.shape
        for fac_idx in range(fac_num):
            self.fac_info.append((facility_df.iloc[fac_idx,1], facility_df.iloc[fac_idx,2]))
        
        for equip_idx in range(equip_type_num):
            fix_time_strs = equipment_df.iloc[equip_idx, 2].split('-')
            self.equip_info[equipment_df.iloc[equip_idx, 0]] = (equipment_df.iloc[equip_idx, 1], (int(fix_time_strs[0]), int(fix_time_strs[1])))

        for fac_idx in range(fac_num):
            for equip_idx in range(equip_type_num):
                num_equip = equipment_df.iloc[equip_idx, fac_idx + 3]
                for equip_iter in range(num_equip):
                    self.equips[(fac_idx, equip_idx, equip_iter)] = (self.equip_info[equipment_df.iloc[equip_idx, 0]], fac_idx)

    def initialize_workers(self, worker_file):
        worker_df = pd.read_csv(worker_file).iloc[:, 1:]
        for idx, row in worker_df.iterrows():
            name = row["Name"]
            certification = row["Equipment Certification(s)"]
            shift = row["Shifts"]
            worker = Worker(name, certification, shift)
            self.workers.append(worker)
    
    def initialize_work_orders(self, workOrder_file, start_time):
        workOrder_df = pd.read_csv(workOrder_file, header=1).iloc[:, 1:]
        for idx, row in workOrder_df.iterrows():
            equipment = row["Equipment Type"]
            priority = row["Priority(1-5)"]
            duration = row["Time to Complete"]
            submission_time = start_time
            work_order = WorkOrder(self.workOrder_id, equipment, priority, duration, submission_time)
            self.workOrder_id += 1
            self.work_orders.append(work_order)

    def update_work_state(self):
        self.agent.do_action(self.work_state)
    
    def one_timestep_passed(self, new=False):
        self.time_step += 1
        if random.random() < 0.2 and new:
            cur_id_str = ''
            for id_d in np.random.randint(0, 9, size=(10)):
                cur_id_str += str(id_d)
            new_equip = random.choice(self.equipment_names)
            new_pri = random.randint(1, 5)
            new_dur = random.randint(1, 20)
            self.work_state.work_orders.append(WorkOrder(cur_id_str,new_equip, new_pri, new_dur, self.time_step))

        jobs = self.work_state.get_jobs(job_status="in progress")
        for job in jobs:
            if job.one_timestep_passed():
                self.work_state.delete_jobs(job.id)

        workers = self.work_state.get_workers()
        for worker in workers:
            worker.one_timestep_passed()
        
        self.agent.do_action(self.work_state)


class Worker:
    def __init__(self, name, certification, shift, status=0):
        self.name = name
        self.certification = certification
        self.shift = shift
        self.status = status

    def __str__(self):
        return "[name: {}; status: {}: certification: {}; shift: {}]".format(self.name, self.status, self.certification, self.shift)
    
    def is_available(self):
        return self.status == 0

    def put_towork(self, hours):
        self.status = hours
    
    def one_timestep_passed(self):
        # Return whether current worker is done his job
        if self.status > 0:
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
        return "[jobid: {}; status: {}; time_rest: {}/{}; equipment: {}; priority: {};  time_waited: {}; submission_time: {}".format(self.id, self.status, self.time_rest, self.duration, self.equipment, self.priority, self.time_waited, self.submission_time)

    def get_dict(self):
        return {"id": self.id, "equipment": self.equipment, "duration": self.duration, "submission_time": self.submission_time, "status": self.status, "time_rest": self.time_rest}

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
            self.time_rest -= 1
            if self.time_rest == 0:
                return True
        elif self.is_pending():
            self.time_waited += 1
        return False
        
    
    

if __name__ == '__main__':
    qLearningAgent = QLearningAgent(0.9, 1e-4, 0.1)
    chevron = Chevron(qLearningAgent, "equipment.csv", "facility.csv", "worker.csv", "workOrder.csv")
    # chevron2 = copy.deepcopy(chevron)
    # chevron2.work_state.workers[0].put_towork(2)
    # print(chevron2.work_state.workers[0].name, chevron2.work_state.workers[0].is_available())
    # print(chevron2.work_state.workers[0].name, chevron.work_state.workers[0].is_available())

