import requests
import json
from PaymentInformation import PaymentInformation
from MaintenanceRequest import MaintenanceRequest
from UnitRequest import UnitRequest
from ApplicationRequest import ApplicationRequest

# ----------------------------- Application Processing -----------------------------

applicationRequest = ApplicationRequest("john1980", "John", "Legend", "430 Campbell Rd, Richardson, Texas 75080",
                                        "972-345-5432", "123-45-6789", "05-May-2020", 12, "123456", "09876543",
                                        "s3.aws.com/propertyBucket/john_DL", "s3.aws.com/propertyBucket/john_PS", "906")


r = requests.post("http://localhost:9998/application-request",
                  headers={"Content-Type":"application/json"},
                  data=json.dumps(applicationRequest.__dict__))

application = r.json()
print(r.json())

r = requests.get("http://localhost:9998/application-request/"+application["body"]["userId"],
                  headers={"Content-Type":"application/json"})
print(r.json())

r = requests.delete("http://localhost:9998/application-request/"+application["body"]["userId"],
                  headers={"Content-Type":"application/json"})
print(r.json())

# ----------------------------- Unit Management        -----------------------------

unitRequest = UnitRequest("906", "1200", 1500.00, 1250.00, 2, 2, "true")

r = requests.post("http://localhost:9998/unit-request",
                  headers={"Content-Type":"application/json"},
                  data=json.dumps(unitRequest.__dict__))

unit = r.json()
print(r.json())

r = requests.get("http://localhost:9998/unit-request/"+unit["body"]["unitNumber"],
                  headers={"Content-Type":"application/json"})
print(r.json())

r = requests.delete("http://localhost:9998/unit-request/"+unit["body"]["unitNumber"],
                  headers={"Content-Type":"application/json"})
print(r.json())

# ----------------------------- Maintenance Request    -----------------------------

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


# ----------------------------- Payment Service        -----------------------------

paymentInfo = PaymentInformation("VISA", "John", "2456098745674326", "345", 1300.00, "john1980")

r = requests.post("http://localhost:9998/payment-processing",
                  headers={"Content-Type":"application/json"},
                  data=json.dumps(paymentInfo.__dict__))

payment = r.json()
print(r.json())

r = requests.get("http://localhost:9998/payment-processing/"+payment["paymentConfirmationNumber"],
                  headers={"Content-Type":"application/json"})
print(r.json())