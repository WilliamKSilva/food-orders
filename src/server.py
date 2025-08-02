from flask import Flask, request

from validator import validate_payload
from requests import REQUEST_ORDER_DATA

app = Flask(__name__)

@app.get("/")
def status():
    return "Server up and running..."

@app.post("/customers")
def create_customers():
    payload = request.get_json()
    print(f"[INFO] Create Customer, JSON: {payload}")
    try:
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