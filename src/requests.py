REQUEST_ORDER_DATA = {
    "customer_id": int,
    "restaurant_id": int,
    "items": list,
    "delivery_address": {
        "cep": str,
        "number": str
    },
}

REQUEST_CUSTOMER_DATA = {
    "name": str,
    "email": str,
    "phone_number": str,
    "default_address": {
        "cep": str,
        "number": str,
        "complement": str
    },
}