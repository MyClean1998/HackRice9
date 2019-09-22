from flask import Flask, request, make_response, render_template
import json
# import simulator
# from chevron import Chevron

app = Flask(__name__)

chevron = None


@app.route("/", methods=['POST'])
def initialize_chevron():
        # chevron = Chevron("equipment.csv", "facility.csv", "worker.csv", "workOrder.csv")
        print("Initialize Backend")
        print(request.form)
        return build_json(chevron)


@app.route("/update", methods=['POST'])
def update_chevron():
        print("Update time")
        new_stuffs = request.form
        return build_json(chevron)

def build_json(chevron, actions=None):
        update_dict = {}

        workers = chevron.work_state.get_available_workers()
        workers_name = list(map(lambda w: w.name, workers))

        pending_jobs = chevron.work_state.get_pending_jobs()
        pending_joblist = [job.get_dict() for job in pending_jobs]
        ip_jobs = chevron.work_state.get_inprogress_jobs()
        ip_joblist = [job.get_dict() for job in ip_jobs]

        if actions is not None:
                actions_list = list(map(lambda a: {"job_id": a[0].id, "worker_name": a[1].name}, actions))
                update_dict["actions"] = actions_list

        update_dict["workers"] = workers_name
        update_dict["work_orders"] = {"pending": pending_joblist, "in_progress": ip_joblist
        update_json = json.dumps(update_dict)
        print(update_json)
        return update_json

        




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)


