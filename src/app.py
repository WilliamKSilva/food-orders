from flask import Flask, request

from models.customer import Customer
from validator import validate_payload
from requests import REQUEST_CUSTOMER_DATA, REQUEST_ORDER_DATA
from conn import initDB 
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

load_dotenv()

engine = initDB()
Session = sessionmaker(engine)

@app.get("/")
def status():
    return "Server up and running..."

@app.post("/customers")
def create_customers():
    payload = request.get_json()
    print(f"[INFO] Create Customer, JSON: {payload}")
    try:
        validate_payload(payload, REQUEST_CUSTOMER_DATA, "create customer:")
        customer = Customer(
            name=payload["name"],
            email=payload["email"],
            phone_number=payload["phone_number"],
            default_address=payload["default_address"]
        )

        with Session() as session:
            session.add(customer)
            session.commit()

        return ({}, 200)
    except Exception as err:
        return (
            {"error": f"{err}", "status": 400},
            400,
        )

@app.post("/orders")
def create_order():
    payload = request.get_json()
    print(f"[INFO] Create Order, JSON: {payload}")
    try:
        validate_payload(payload, REQUEST_ORDER_DATA, "create order:")

        return ({}, 200)
    except Exception as err:
        return (
            {"error": f"{err}", "status": 400},
            400,
        )