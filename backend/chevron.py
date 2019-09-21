import random
import pandas as pd

class Chevron:
    def __init__(self, equipment_file, facility_file, worker_file, workOrder_file):

        self.equip_failure_prob = {}

    def initialize_facility_equipment(self, equipment_file, facility_file):
        equipment_df = pd.read_csv(equipment_file)
        facility_df = pd.read_csv(facility_file)
        print(equipment_df)
        print(facility_df)


class Equipment:
    equipment_failure_prob = {"Pump": 0.008695652174, "Compressor": 0.04347826087, "Seperator": 0.1304347826,
                              "Sensor": 0.08695652174, "Security": 0.147826087, "Electricity": 0.1652173913,
                              "Networking": 0.01739130435, "Vehicle": 0.2434782609, "HVAC": 0.1130434783,
                              "Conveyer": 0.04347826087}
    equipment_fixing_time = {"Pump": [1, 12], "Compressor": [2, 13], "Seperator": [3, 5],
                              "Sensor": [1, 2], "Security": [1, 2], "Electricity": [1, 5],
                              "Networking": [1, 3], "Vehicle": [3, 8], "HVAC": [4, 24],
                              "Conveyer": [5, 10]}

    def __init__(self, name, probFailure, fixingTime, status="idle"):
        self.name = name
        self.probFailure = probFailure
        self.fixingTime = fixingTime
        self.status = status

    def get_fixingTime(self):
        return random.randint(*self.fixingTime)


class Facility:
    def __init__(self, position, fac_equipment):
        self.position = position
        self.equipments = fac_equipment


class Worker:
    def __init__(self):
        pass

class WorkOrder:
    def __init__(self):
        pass

if __name__ == '__main__':
    chevron = Chevron()
