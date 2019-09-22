import time
from chevron import Chevron
from qlearningAgent import QLearningAgent


def run_simulation():
        qLearningAgent = QLearningAgent(0.9, 1e-4, 0.1)
        chevron = Chevron(qLearningAgent, "equipment.csv", "facility.csv", "worker.csv", "workOrder.csv")
        chevron.initialize()
        start_time = time.time()
        time_step = 0
        print("Current time step: {}".format(time_step))
        print(chevron)
        while True:
                if time.time() - start_time >= 5:
                        time_step += 1
                        print("Current time step: {}".format(time_step))
                        chevron.one_timestep_passed()
                        print(chevron)
                        start_time = time.time()

if __name__ == "__main__":
    run_simulation()
