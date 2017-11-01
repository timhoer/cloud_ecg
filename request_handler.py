import sys
sys.path.insert(0, './bme590hrm/Code')
from flask import Flask, request, jsonify
from classy_hrm import classy_hrm
from ecg import ECG
app = Flask(__name__)
calls = 0


@app.route("/requests", methods=['GET'])
def request_total():
    """
    :return: the total number of requests the service has served since its
    most recent reboot as JSON
    """
    global calls
    calls += 1
    output = {"requests": calls}
    return jsonify(output)


@app.route("/heart_rate/summary", methods=['POST'])
def request_summary():
    """
    Takes in JSON input "time" and "voltage."

    :return: instantaneous HR and brady/tachy summary in the following form:
            {   "time": [1, 2, 3, ...],
                "instantaneous_heart_rate": [100, 60, 62, ...],
                "tachycardia_annotations": [true, false, false, ...],
                "bradycardia_annotations": [false, false, false, ...],
            }
    """
    global calls
    calls += 1
    time = request.json['time']
    voltage = request.json['voltage']
    data = ECG(time=time, voltage=voltage)
    output = data.get_summary()
    return jsonify(output)


@app.route("/heart_rate/average", methods=['POST'])
def request_average():
    """
    Takes in JSON input "averaging_period", "time," and "voltage."

    :return: instantaneous HR and brady/tachy summary in the following form:
            {
                "averaging_period": 20,
                "time_interval": [1, 2, 3, ...],
                "instantaneous_heart_rate": [100, 60, 62, ...],
                "tachycardia_annotations": [true, false, false, ...],
                "bradycardia_annotations": [false, false, false, ...],
            }
    """
    global calls
    calls += 1
    try:
        window = request.json['averaging_period']
        file_input= request.json['file']
        tachy_max = request.json['tachy_max']
        brady_min = request.json['brady_min']
    except:
        output = "input data incorrectly formatted. Please try again"
        return jsonify(output), 400
    try:
        data = ECG(window=window, tachy_max=tachy_max, brady_min=brady_min, file_input=file_input)
        output = data.get_average()
    except:
        output = "Internal error. Please try again later"
        return jsonify(output)   

