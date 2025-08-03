import datetime
from flask import Flask, request

from models.customer import Customer
from models.order import Order, OrderStatus, OrderItem
from models.restaurant import RestaurantMenuItem
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
            customer_id = customer.id 

        return (
            {
                "customer_id": customer_id
            }, 
            200
        )
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
        order = Order(
           status=OrderStatus.CREATED.value,
           payment_method=payload["payment_method"],
           customer_id=payload["customer_id"],
           restaurant_id=payload["restaurant_id"],
           delivery_address=payload["delivery_address"]
        )

        with Session() as session:
            order_items: list[OrderItem] = []
            total_cost = 0.0
            for i in payload["items"]:
                menu_item = session.get(RestaurantMenuItem, i["product_id"])
                if not menu_item:
                    raise Exception(f"Menu item {i['product_id']} not found")
                order_item = OrderItem(
                    menu_item_id=menu_item.id,
                    quantity=i["quantity"],
                    price=menu_item.price
                )
                order_items.append(order_item)
                total_cost += menu_item.price * i["quantity"]

            order.total_cost = total_cost
            session.add(order)
            order.order_items = order_items
            session.commit()
            order_id = order.id

        delivery_time = datetime.datetime.now() + datetime.timedelta(minutes=45)
        return ({
            "order_id": order_id,
            "status": order.status.value,
            "delivery_time": delivery_time.strftime("%Y-%m-%d %H:%M:%S")
        }, 200)
    except Exception as err:
        print(f"[ERROR] {err}")
        return (
            {"error": "internal server error", "status": 400},
            400,
        )