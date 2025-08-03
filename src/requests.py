from models.order import OrderPaymentMethod

REQUEST_ORDER_DATA = {
    "customer_id": int,
    "restaurant_id": int,
    "items": list,
    "payment_method": OrderPaymentMethod,
    "delivery_address": {
        "cep": str,
        "number": str,
        "complement": str
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