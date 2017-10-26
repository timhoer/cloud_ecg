from flask import Flask, request, jsonify
app= Flask(__name__)


@app.route("/requests", methods=['GET'])
def request_total():
    """
    :return: the total number of requests the service has served since its
    most recent reboot as JSON
    """


@app.route("/heart_rate/summary", methods=['POST'])
def request_summary(time,voltage):
    """
    Takes in JSON input "time" and "voltage."

    :return: instantaneous HR and brady/tachy summary in the following form:
            {   "time": [1, 2, 3, ...],
                "instantaneous_heart_rate": [100, 60, 62, ...],
                "tachycardia_annotations": [true, false, false, ...],
                "bradycardia_annotations": [false, false, false, ...],
            }
    """
    time = request.json['time']
    voltage = request.json['voltage']



@app.route("/add", methods=['POST'])
def return_average():
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
    window = request.json['averaging_period']
    time = request.json['time']
    voltage = request.json['voltage']

