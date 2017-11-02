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

    :return: instantaneous HR and brady/tachy summary as JSON in the following form:
            {   "time": [1, 2, 3, ...],
                "instantaneous_heart_rate": [100, 60, 62, ...],
                "tachycardia_annotations": [true, false, false, ...],
                "bradycardia_annotations": [false, false, false, ...],
            }
    """
    global calls
    calls += 1
    try:
        time = request.json['time']
        voltage = request.json['voltage']
    except:
        output = "Input data incorrectly formatted. Please try again."
        return jsonify(output), 400
    try:
        data = ECG(time=time, voltage=voltage)
        output = data.get_summary()
        return jsonify(output)
    except:
        output = "Internal error. Please try again later."
        return jsonify(output), 500


@app.route("/heart_rate/average", methods=['POST'])
def request_average():
    """
    Takes in JSON input "averaging_period", "time," and "voltage."

    :return: instantaneous HR and brady/tachy summary as JSON in the following form:
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
        time = request.json['time']
        voltage = request.json['voltage']
    except:
        output = "Input data incorrectly formatted. Please try again."
        return jsonify(output), 400
    try:
        data = ECG(window=window, time=time, voltage=voltage)
        output = data.get_average()
        return jsonify(output)
    except:
        output = "Internal error. Please try again later."
        return jsonify(output), 500
