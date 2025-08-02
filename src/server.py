from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def status():
    return "Server up and running..."

EXPECTED_ORDER_DATA = {
    "customer_id": int,
    "restaurant_id": int,
    "items": list,
    "delivery_address": str,
}

@app.post("/orders")
def create_order():
    payload = request.get_json()
    print(f"[INFO] Create Order, JSON: {payload}")
    try:
        validate_payload("create order", EXPECTED_ORDER_DATA, payload)

        return ({}, 200)
    except Exception as err:
        return (
            {"error": f"{err}", "status": 400},
            400,
        )

def validate_payload(method: str, schema: dict[str, any], payload: dict):
    # Validate missing fields
    keys = set(payload.keys())
    schema_keys = set(schema.keys())
    errorMessage = f"{method}: "
    hasError = False

    if keys != schema_keys:
        missing_fields = schema_keys.difference(keys)
        additional_fields = keys.difference(schema_keys)

        if len(missing_fields) > 0:
            errorMessage += f"Missing fields: {missing_fields} "

        if len(additional_fields) > 0:
            errorMessage += f"Additional fields: {additional_fields}"
        
        hasError = True

    # On missing fields throw the error right away
    if hasError:
        raise Exception(errorMessage)

    # Validate wrong data types for a valid payload
    errorMessage += f"fields have wrong type: ["
    payload_items = payload.items()
    wrong_types = {}
    for k, v in payload_items:
        expected_type = schema[k]
        found_type = type(v)
        if expected_type != found_type:
            wrong_types[k] = {
                "found_type": found_type,
                "expected_type": expected_type
            }

    if len(wrong_types) > 0:
        hasError = True

    for i, (k, v) in enumerate(wrong_types.items()):
        found_type = v["found_type"]
        expected_type = v["expected_type"]
        field_name = k
        last_index = i == len(wrong_types) - 1
        errorMessage += f"\\{field_name}\\ 'expected': {expected_type} -> 'found': {found_type}"

        if last_index:
            errorMessage += "]"
        else:
            errorMessage += ", "
        
    if hasError:
        raise Exception(errorMessage)