import requests
import json
from PaymentInformation import PaymentInformation


paymentInfo = PaymentInformation("VISA", "John", "2456098745674326", "345", 1300.00, "john1980")

r = requests.post("http://localhost:9998/payment-processing",
                  headers={"Content-Type":"application/json"},
                  data=json.dumps(paymentInfo.__dict__))

payment = r.json()
print(r.json())

r = requests.get("http://localhost:9998/payment-processing/"+payment["paymentConfirmationNumber"],
                  headers={"Content-Type":"application/json"})
print(r.json())