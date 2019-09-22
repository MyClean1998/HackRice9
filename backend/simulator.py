import time
from chevron import Chevron
from qlearningAgent import QLearningAgent


def run_simulation():
        qLearningAgent = QLearningAgent(0.9, 3e-4, 0.1)
        start_time = time.time()
        time_step = 0
        print("Current time step: {}".format(time_step))
        for i in range(200):
                chevron = Chevron(qLearningAgent, "equipment.csv", "facility.csv", "worker.csv", "workOrder.csv")
                chevron.initialize()
                loss = 0
                while chevron.work_state.work_orders:
                        # if time.time() - start_time >= 5:
                        if True:
                                time_step += 1
                                chevron.one_timestep_passed(new=True)
                                loss += sum([job.priority for job in chevron.work_state.work_orders])
                                start_time = time.time()
                if i % 20 == 0:
                        chevron = Chevron(qLearningAgent, "equipment.csv", "facility.csv", "worker.csv", "workOrder.csv")
                        chevron.initialize()
                        loss = 0
                        while chevron.work_state.work_orders:
                                # if time.time() - start_time >= 5:
                                if True:
                                        time_step += 1
                                        chevron.one_timestep_passed(new=False)
                                        loss += sum([job.priority for job in chevron.work_state.work_orders])
                                        start_time = time.time()
                        print('Loss: %d' % loss)

if __name__ == "__main__":
    run_simulation()
