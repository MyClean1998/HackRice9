
class Chevron:
    def __init__(self):
        pass


class Equipment:
    equipment_failure_prob = {"Pump": 0.008695652174, "Compressor": 0.04347826087, "Seperator": 0.1304347826,
                              "Sensor": 0.08695652174, "Security": 0.147826087, "Electricity": 0.1652173913,
                              "Networking": 0.01739130435, "Vehicle": 0.2434782609, "HVAC": 0.1130434783,
                              "Conveyer": 0.04347826087}
    equipment_fixing_time = {"Pump": [1, 12], "Compressor": [2, 13], "Seperator": [3, 5],
                              "Sensor": [1, 2], "Security": [1, 2], "Electricity": [1, 5],
                              "Networking": [1, 3], "Vehicle": [3, 8], "HVAC": [4, 24],
                              "Conveyer": [5, 10]}

    def __init__(self, name, status="idle"):
        self.name = name
        self.probFailure = Equipment.get_failure_prob(name)
        self.fixingTime = Equipment.get_failure_prob(name)
        self.status = status

    @staticmethod
    def get_failure_prob(name):
        return Equipment.equipment_failure_prob[name]

    @staticmethod
    def get_fixing_time(name):
        return Equipment.equipment_fixing_time[name]


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