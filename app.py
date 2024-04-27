from flask import Flask, request, jsonify
import datetime
from data_validator import DataValidator
from data_repo import DataRepository

app = Flask(__name__)


@app.post('/data')
def receive_data():
    data = request.json
    validation_errors = DataValidator.validate(data)
    if validation_errors:
        return jsonify({"status": "failure", "errors": validation_errors}), 400
    timestamp = data['czas']
    DataRepository.save_data(timestamp, data)
    return jsonify({"status": "success", "data": data}), 200


@app.get('/data/<timestamp>')
def get_data(timestamp):
    requested_time = datetime.datetime.fromisoformat(timestamp)
    nearest_data = DataRepository.get_nearest_data(requested_time)
    return jsonify(nearest_data)


if __name__ == '__main__':
    app.run(debug=False)
