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

    def get_q_features(self):
        pass