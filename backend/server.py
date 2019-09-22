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
        update_dict["workers"] = {}
        update_dict["work_orders"] = {}
        update_dict["actions"] = {}

        # workers = chevron.get_workers()
        # work_orders = chevron.get_work_orders()
        if actions is not None:
                pass
        update_json = json.dumps(update_dict)
        return update_json

        




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)


