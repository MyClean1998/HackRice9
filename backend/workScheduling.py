import time


class WorkSchedulingState:

    def __init__(self, workers=[], facilities=[], work_orders=[]):
        self.workers = workers 
        self.facilities = facilities 
        self.work_orders = work_orders

    def get_available_worker(self, equipment):
        return filter(lambda w: (equipment in w.certification) and (w.is_available()), self.workers)
    
    def get_available_facilities(self, equipment):
        return filter(lambda f: f.has_available_equipment(equipment), self.facilities)

    def get_worker_job_pairs(self):
        actions = []
        for work in self.work_orders:
            equip = work.equipment
            for fclt in self.get_available_facilities(equip):
                for worker in self.get_avaliable_workers(equip):
                    actions.append((work, fclt, worker))
        return actions
        