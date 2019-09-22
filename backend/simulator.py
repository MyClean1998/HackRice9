import time
from chevron import Chevron
import tensorflow as tf
from qlearningAgent import QLearningAgent


def run_simulation():
        sess = tf.Session()
        
        start_time = time.time()
        agent = QLearningAgent(0.9, 1e-5, 0.0, 1000, sess, True)
        
        # init = tf.global_variables_initializer()
        # sess.run(init)
        # print(chevron)
        for i in range(100):
                chevron = Chevron(agent, "equipment.csv", "facility.csv", "worker.csv", "workOrder.csv", is_training=True)
                chevron.initialize()
                time_step = 0
                loss = 0
                # print("Current time step: {}".format(time_step))
                while chevron.work_state.get_jobs():
                        # if time.time() - start_time >= 0.05:
                        if True:
                                time_step += 1
                                chevron.one_timestep_passed(new=True)
                                loss += sum([job.priority for job in chevron.work_state.work_orders])
                                start_time = time.time()
                if i % 10 == 0:
                        chevron = Chevron(agent, "equipment.csv", "facility.csv", "worker.csv", "workOrder.csv", is_training=True)
                        chevron.initialize()
                        time_step = 0
                        loss = 0
                        # print("Current time step: {}".format(time_step))
                        while chevron.work_state.get_jobs():
                                # if time.time() - start_time >= 0.05:
                                if True:
                                        time_step += 1
                                        chevron.one_timestep_passed()
                                        loss += sum([job.priority for job in chevron.work_state.work_orders])
                                        start_time = time.time()
                        print("Iterations spent in this training period is %d" % loss)

if __name__ == "__main__":
    run_simulation()
