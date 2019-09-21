import time


class WorkSchedulingState:

    def __init__(self, pendingJobs, idleWorkers, idleEquipments, finishedJobs):
        self.pendingJobs = pendingJobs
        self.idleWorkers = idleWorkers
        self.idleEquipments = idleEquipments
        self.finishedJobs = finishedJobs
        self.time = time.time()
    
    def get_worker_job_pairs(self):
        pass
    
    def get_a_features(self):
        pass