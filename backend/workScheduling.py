import time
from copy import deepcopy


class WorkSchedulingState:

    def __init__(self, workers=[], facilities=[], work_orders=[]):
        self.workers = workers 
        self.facilities = facilities 
        self.work_orders = work_orders

    def __str__(self):
        job_string = list(map(lambda j: str(j), self.get_jobs()))
        return_str = "\tCurrent Jobs: \n\t\t" + "\n\t\t".join(job_string)
        worker_string = list(map(lambda w: str(w), self.get_workers()))
        return_str += "\n\tCurrent Workers: \n\t\t" + "\n\t\t".join(worker_string)
        return return_str

    def get_workers(self):
        return self.workers

    def get_available_workers(self, equipment):
        return list(filter(lambda w: (equipment in w.certification) and (w.is_available()), self.workers))

    def get_facilities(self):
        return self.facilities
    
    def get_available_facilities(self, equipment):
        return list(filter(lambda f: f.has_available_equipment(equipment), self.facilities))

    def get_equipment_list(self):
        return self.facilities[0].equipments.keys()

    def get_pending_jobs(self):
        return list(filter(lambda o: o.is_pending(), self.work_orders))

    def get_inprogress_jobs(self):
        return list(filter(lambda o: o.is_in_progress(), self.work_orders))

    def get_jobs(self, job_status=None):
        if job_status is None:
            return self.work_orders
        elif job_status == "pending":
            return self.get_pending_jobs()
        elif job_status == "in progress":
            return self.get_inprogress_jobs()

    def get_jobs_with_equip(self, job_status=None):
        jobs = self.get_jobs(job_status)
        equipments = self.get_equipment_list()
        equip_job_map = {}
        for equip in equipments:
            equip_job_map[equip] = list(filter(lambda j: j.equipment == equip, jobs))
        return equip_job_map
    
    def delete_jobs(self, job_id):
        jobs = self.get_jobs()
        new_jobs = []
        for job in jobs:
            if job.id != job_id:
                new_jobs.append(job)
        self.work_orders = new_jobs

    def set_evoke_func(self, evoke_func):
        self.evoke_agent = evoke_func

    def update_state(self, action):
        job, fac, worker = action
        fac.put_equipment_towork(job.equipment, job.duration)
        worker.put_towork(job.duration)
        job.put_in_progress()

    def get_worker_job_pairs(self):
        actions = []
        for work in self.get_jobs(job_status="pending"):
            equip = work.equipment
            for fclt in self.get_available_facilities(equip):
                for worker in self.get_available_workers(equip):
                    actions.append((work, fclt, worker))
        return actions
    
    def get_reward(self):
        cost = 0
        for work in self.work_orders:
            cost += work.priority * (work.time_waited + work.time_rest)
        return -cost

    def generate_action(self):
        # TODO: this function will be called when the state changed
        state = deepcopy(self)
        