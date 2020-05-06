import requests
import json
from PaymentInformation import PaymentInformation
from MaintenanceRequest import MaintenanceRequest



# ----------------------------- Maintenance Request  -----------------------------

maintenanceRequest = MaintenanceRequest("PLUMBING", "05-May-2020", "03-May-2020",
                                        "plumbing issue in master bathroom",
                                        "john1980", "NOT STARTED")

r = requests.post("http://localhost:9998/maintenance-request",
                  headers={"Content-Type":"application/json"},
                  data=json.dumps(maintenanceRequest.__dict__))

maintenance = r.json()
print(r.json())

r = requests.get("http://localhost:9998/maintenance-request/"+maintenance["body"]["userId"],
                  headers={"Content-Type":"application/json"})
print(r.json())


# ----------------------------- Payment Service      -----------------------------

paymentInfo = PaymentInformation("VISA", "John", "2456098745674326", "345", 1300.00, "john1980")

r = requests.post("http://localhost:9998/payment-processing",
                  headers={"Content-Type":"application/json"},
                  data=json.dumps(paymentInfo.__dict__))

payment = r.json()
print(r.json())

r = requests.get("http://localhost:9998/payment-processing/"+payment["paymentConfirmationNumber"],
                  headers={"Content-Type":"application/json"})
print(r.json())