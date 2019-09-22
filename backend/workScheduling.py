import time


class WorkSchedulingState:

    def __init__(self, workers=[], facilities=[], work_orders=[]):
        self.workers = workers 
        self.facilities = facilities 
        self.work_orders = work_orders

    def get_available_workers(self, equipment):
        return filter(lambda w: (equipment in w.certification) and (w.is_available()), self.workers)
    
    def get_available_facilities(self, equipment):
        return filter(lambda f: f.has_available_equipment(equipment), self.facilities)

    def get_equipment_list(self):
        return self.facilities[0].equipments.keys()

    def get_pending_jobs(self):
        return filter(lambda o: o.is_pending(), self.work_orders)

    def get_inprogress_jobs(self):
        return filter(lambda o: o.is_in_progress(), self.work_orders)

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
            equip_job_map[equip] = filter(lambda j: j.equipment == equip, jobs)
        return equip_job_map

    def update_state(self, action):
        job, fac, worker = action
        fac.put_equipment_towork(job.equipment, job.duration)
        worker.put_towork(job.duration)
        job.put_in_progress()

    def get_worker_job_pairs(self):
        actions = []
        for work in self.work_orders:
            equip = work.equipment
            for fclt in self.get_available_facilities(equip):
                for worker in self.get_avaliable_workers(equip):
                    actions.append((work, fclt, worker))
        return actions
    
    def get_reward(self):
        cost = 0
        for work in self.work_orders:
            cost += work.priority * (work.waited_time + work.time_rest)
        return -cost
        