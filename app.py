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

# ----------------------------- Maintenance Request  -----------------------------

@app.route("/maintenance-request", methods=["POST"])
def maintenance_request():
    body = request.json
    body["requestId"] = str(uuid.uuid1())

    maintenance_requests.append(body)
    print(type(body))
    return json.dumps({"result": "success", "body": body})

@app.route("/maintenance-request/<id>", methods=["GET"])
def get_maintenance_request(id):
    x = maintenance_requests
    print(x)
    return json.dumps(maintenance_requests[0])

# ----------------------------- Payment Service      -----------------------------


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



