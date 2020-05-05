from flask import Flask, jsonify, request
import os
import uuid
import json
from datetime import datetime
from PaymentResponse import PaymentResponse

app = Flask(__name__)

PORT = os.getenv("PORT")

paymentHistories = []

@app.route("/payment-processing", methods=["POST"])
def process_payment():
    body = request.json
    body["paymentConfirmationNumber"] = str(uuid.uuid1())
    body["paymentDate"] = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    body["sucessFlag"] = "success"

    payment_response = PaymentResponse(body['paymentConfirmationNumber'], body['sucessFlag'])

    paymentHistories.append(body)
    print (paymentHistories[0])
    return (json.dumps(payment_response.__dict__))

@app.route("/payment-processing/<id>", methods=["GET"])
def get_payment_record(id):
    return jsonify(paymentHistories[0])

if __name__ == "__main__":
    app.run(debug=False, port=9998, host="localhost")



