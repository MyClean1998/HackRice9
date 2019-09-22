import time


class WorkSchedulingState:

    def __init__(self, pendin_jobs, idle_workers, idle_equipments, finished_jobs):
        self.workers = None 
        self.facilities = None 
        self.work_orders = None

    def set_work_order(self, work_orders):
        self.work_orders = work_orders
    
    def set_workers(self, workers):
        self.workers = workers
    
    def set_facilities(self, facilities):
        self.facilities = facilities

    def get_worker_job_pairs(self):
        actions = []
        for work in self.work_orders:
            equip = work.equipment
            for fclt in self.facilities:
                if fclt.has_equipment(equip):
                    for worker in self.workers:
                        if equip in worker.certification:
                            actions.append((work, fclt, worker))
        return actions
        