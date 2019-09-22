import time
from chevron import Chevron

def run_simulation():
        chevron = Chevron(sess, "equipment.csv", "facility.csv", "worker.csv", "workOrder.csv", is_training=True)
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
