import datetime
from enum import Enum
from sqlalchemy import ForeignKey, Enum as SQLEnum 
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.restaurant import Restaurant, RestaurantMenuItem
from models.customer import Customer 

class OrderStatus(Enum):
    CREATED = "CREATED"
    ACCEPTED = "ACCEPTED"
    PREPARING = "PREPARING"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

class OrderPaymentMethod(Enum):
    CREDIT_CARD = "CREDIT_CARD"
    PIX = "PIX"
    CASH = "CASH"

class Order(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped["OrderStatus"] = mapped_column(SQLEnum(OrderStatus, name="orderstatus"))
    payment_method: Mapped["OrderPaymentMethod"] = mapped_column(SQLEnum(OrderPaymentMethod, name="orderpaymentmethod"))
    total_cost: Mapped[float]
    delivery_address: Mapped[dict[str, any]]

    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurant.id"))
    restaurant: Mapped["Restaurant"] = relationship()

    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped["Customer"] = relationship()

    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order", cascade="all, delete-orphan"
    )

    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())

class OrderItem(Base):
    __tablename__ = "order_item"
    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int]
    price: Mapped[float]

    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    order: Mapped["Order"] = relationship(back_populates="order_items")

    menu_item_id: Mapped[int] = mapped_column(ForeignKey("restaurant_menu_item.id"))
    menu_item: Mapped["RestaurantMenuItem"] = relationship(back_populates="order_items")

    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())