import datetime
import enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.restaurant import RestaurantMenuItem 
from models.customer import Customer 

class OrderStatus(enum.Enum):
    PENDING = "CREATED"
    ACCEPTED = "ACCEPTED"
    PREPARING = "PREPARING"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

class OrderPaymentMethod(enum.Enum):
    CREDIT_CARD = "CREDIT_CARD"
    PIX = "PIX"
    CASH = "CASH"

class Order(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped["OrderStatus"]
    payment_method: Mapped["OrderPaymentMethod"]
    total_cost: Mapped[float]
    delivery_address: Mapped[dict[str, any]]
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id")) 
    customer: Mapped["Customer"] = relationship()
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurant.id")) 
    restaurant: Mapped["Customer"] = relationship()
    order_items: Mapped[list["OrderItem"]] = relationship()
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())

class OrderItem(Base):
    __tablename__ = "order_item"
    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int]
    price: Mapped[float]
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    order: Mapped["Order"] = relationship()
    menu_item_id: Mapped[int] = mapped_column(ForeignKey("restaurant_menu_item.id"))
    menu_item: Mapped["RestaurantMenuItem"] = relationship()
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())