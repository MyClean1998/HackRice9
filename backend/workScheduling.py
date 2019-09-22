import time
from copy import deepcopy
import ast


class WorkSchedulingState:

    def __init__(self, workers, equips, work_orders, equip_info, fac_info):
        self.workers = workers
        self.equips = equips
        self.work_orders = work_orders
        self.equip_info = equip_info
        self.fac_info = fac_info

    def __str__(self):
        job_string = list(map(lambda j: str(j), self.get_jobs()))
        return_str = "\tCurrent Jobs: \n\t\t" + "\n\t\t".join(job_string)
        worker_string = list(map(lambda w: str(w), self.get_workers()))
        return_str += "\n\tCurrent Workers: \n\t\t" + "\n\t\t".join(worker_string)
        return return_str

    def get_workers(self):
        return self.workers
    
    def get_available_workers(self, equipment=None):
        if equipment is None:
            func = lambda w: w.is_available()
        else:
            func = lambda w: (equipment in w.certification) and (w.is_available())
        return list(filter(func, self.workers))
    
    def add_workers(self, new_workers):
        json = ast.literal_eval(new_workers)
        print(json)


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
        equip_job_map = {}
        for equip in self.equip_info.keys():
            equip_job_map[equip] = list(filter(lambda j: j.equipment == equip, jobs))
        return equip_job_map
    
    def delete_jobs(self, job_id):
        jobs = self.get_jobs()
        new_jobs = []
        for job in jobs:
            
            if job.id != job_id:
                new_jobs.append(job)
        self.work_orders = new_jobs

    def update_state(self, action):
        job, worker = action
        worker.put_towork(job.duration)
        job.put_in_progress()

    def get_worker_job_pairs(self):
        actions = []
        for work in self.get_jobs(job_status="pending"):
            for worker in self.get_available_workers(work.equipment):
                actions.append((work, worker))
        return actions
    
    def get_reward(self):
        cost = 0
        for work in self.work_orders:
            cost += work.priority * (work.time_waited + work.time_rest)
        return -0.1 * cost

    # def generate_action(self):
    #     # TODO: this function will be called when the state changed
    #     state = deepcopy(self)
        