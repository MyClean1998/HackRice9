import random
import pandas as pd
from workScheduling import WorkSchedulingState


class Chevron:
    def __init__(self, equipment_file, facility_file, worker_file, workOrder_file):
        self.equip_failure_prob = {}
        self.equip_fixing_time = {}

        self.fac_loc = {}
        self.fac_equip_info = {}

        self.workOrder_id = 1

        self.load_facility_equipment_info(equipment_file, facility_file)
        facilities = self.initialize_facility()
        workers = self.initialize_workers(worker_file)
        work_orders = self.initialize_work_orders(workOrder_file)
        self.work_state = WorkSchedulingState(workers, facilities, work_orders)


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
    
    def initialize_work_orders(self, workOrder_file):
        work_orders = []
        workOrder_df = pd.read_csv(workOrder_file, header=1).iloc[:, 1:]
        for idx, row in workOrder_df.iterrows():
            equipment = row["Equipment Type"]
            priority = row["Priority(1-5)"]
            duration = row["Time to Complete"]
            submission_time = row["Submission Timestamp"]
            work_order = WorkOrder(self.workOrder_id, equipment, priority, duration, submission_time)
            self.workOrder_id += 1
            work_orders.append(work_order)
        return work_orders

    def update_work_state(self, action):
        pass
    
    def 



class Equipment:
    def __init__(self, name, id, prob_failure, fixing_time, status=0):
        self.name = name
        self.prob_failure = prob_failure
        self.fixing_time = fixing_time
        self.status = status

    def get_fixing_time(self):
        return random.randint(*self.fixing_time)

    def put_towork(self, hours):
        self.status = hours
    
    def is_available(self):
        return self.status == 0


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
        # print(self.equipments)

    def has_available_equipment(self, equip_name):
        for equip in self.equipments[equip_name]:
            if equip.is_available():
                return True
        return False

    def put_equipment_towork(self, equip_name, hours):
        for equip in self.equipments[equip_name]:
            if equip.is_available():
                equip.put_towork(hours)


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
    

class WorkOrder:
    def __init__(self, id, equipment, priority, duration, submission_time, status="pending"):
        self.id = id
        self.equipment = equipment
        self.priority = priority
        self.duration = duration
        self.submission_time = submission_time
        self.status = status
    
    def is_pending(self):
        return self.status == "pending"
    
    def is_in_progress(self):
        return self.status == "in progress"
    
    def is_finished():
        return self.status == "finished"


if __name__ == '__main__':
    chevron = Chevron("equipment.csv", "facility.csv", "worker.csv", "workOrder.csv")
