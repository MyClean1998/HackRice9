from flask import Flask, request, make_response, render_template
from qlearningAgent import QLearningAgent
import json
import ast
from chevron import Chevron

app = Flask(__name__)

chevron = None
time_step = 0
verbose = True


@app.route("/", methods=['POST'])
def initialize_chevron():
        global chevron
        global time_step
        global verbose

        qLearningAgent = QLearningAgent(0.9, 1e-4, 0.1)
        chevron = Chevron(qLearningAgent, "equipment.csv", "facility.csv", "worker.csv", "workOrder.csv")
        chevron.initialize()

        print("Initialize Backend")
        new_workers = parse_json(request.form)
        chevron.add_workers(new_workers) 
        if verbose:
                print("Current time step: {}".format(time_step))
                print(chevron)
                print("=" * 30)
        return build_json(chevron)


@app.route("/update", methods=['POST'])
def update_chevron():
        global chevron
        global time_step
        global verbose

        # Process new workers (if any)
        new_workers = parse_json(request.form)
        chevron.add_workers(new_workers)    

        actions = chevron.one_timestep_passed(new=False)
        if verbose:
                print("Current time step: {}".format(time_step))
                print(chevron)
                print("=" * 30)
        return build_json(chevron, actions)


def build_json(chevron, actions=[]):
        update_dict = {}

        workers = chevron.work_state.get_available_workers()
        workers_name = list(map(lambda w: w.get_dict(), workers))

        pending_jobs = chevron.work_state.get_pending_jobs()
        pending_joblist = [job.get_dict() for job in pending_jobs]
        ip_jobs = chevron.work_state.get_inprogress_jobs()
        ip_joblist = [job.get_dict() for job in ip_jobs]

        actions_list = list(map(lambda a: {"job_id": a[0].id, "worker_name": a[1].name}, actions))
        update_dict["actions"] = actions_list

        update_dict["workers"] = workers_name
        update_dict["work_orders"] = {"pending": pending_joblist, "in_progress": ip_joblist}
        update_json = json.dumps(update_dict)
        # print(update_json)
        return update_json


def parse_json(new_workers):
        # new_workers = {'{"new_workers":[{"certifates":["Sensor","Security","Networking"],"name":"Bob","shift":"Morning"}]}': ''}
        string = list(new_workers.to_dict().keys())[0]
        # print(string)
        dictionary = ast.literal_eval(string)
        return dictionary["new_workers"]


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)


