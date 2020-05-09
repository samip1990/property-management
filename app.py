from flask import Flask, jsonify, request
import os
import uuid
import json
from datetime import datetime
from PaymentResponse import PaymentResponse

app = Flask(__name__)

PORT = os.getenv("PORT")

payment_histories = []
maintenance_requests = []
unit_requests = []
applicant_requests = []

# ----------------------------- Application Processing -----------------------------

@app.route("/application-request", methods=["POST"])
def application_request():
    body = request.json
    applicant_requests.append(body)
    return json.dumps({"result": "success", "body": body})

@app.route("/application-request/<id>", methods=["GET"])
def get_application(id):
    x = applicant_requests
    return json.dumps(applicant_requests[0])

@app.route("/application-request/<id>", methods=["DELETE"])
def delete_application(id):
    x = applicant_requests
    del applicant_requests[:]
    return json.dumps({"result": "DELETED", "RequestType": "APPLICANT", "userId": id})

# ----------------------------- Unit Management        -----------------------------

@app.route("/unit-request", methods=["POST"])
def unit_request():
    body = request.json
    unit_requests.append(body)
    return json.dumps({"result": "success", "body": body})

@app.route("/unit-request/<id>", methods=["GET"])
def get_unit(id):
    x = unit_requests
    return json.dumps(unit_requests[0])

@app.route("/unit-request/<id>", methods=["DELETE"])
def delete_unit(id):
    x = unit_requests
    del unit_requests[:]
    return json.dumps({"result": "DELETED", "RequestType": "UNIT", "unitNumber": id})

# ----------------------------- Maintenance Request    -----------------------------

@app.route("/maintenance-request", methods=["POST"])
def maintenance_request():
    body = request.json
    body["requestId"] = str(uuid.uuid1())

    maintenance_requests.append(body)
    return json.dumps({"result": "success", "body": body})

@app.route("/maintenance-request/<id>", methods=["GET"])
def get_maintenance_request(id):
    x = maintenance_requests
    return json.dumps(maintenance_requests[0])

# ----------------------------- Payment Service        -----------------------------


@app.route("/payment-processing", methods=["POST"])
def process_payment():
    body = request.json
    body["paymentConfirmationNumber"] = str(uuid.uuid1())
    body["paymentDate"] = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    body["sucessFlag"] = "success"

    payment_response = PaymentResponse(body['paymentConfirmationNumber'], body['sucessFlag'])

    payment_histories.append(body)
    return (json.dumps(payment_response.__dict__))

@app.route("/payment-processing/<id>", methods=["GET"])
def get_payment_record(id):
    return jsonify(payment_histories[0])

if __name__ == "__main__":
    app.run(debug=False, port=9998, host="localhost")



