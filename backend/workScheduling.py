import time


class WorkSchedulingState:
    def __init__(self, pendingJobs, idleWorkers, idleEquipments, finishedJobs):
        self.pendingJobs = pendingJobs
        self.idleWorkers = idleWorkers
        self.idleEquipments = idleEquipments
        self.finishedJobs = finishedJobs

        self.time = time.time()
