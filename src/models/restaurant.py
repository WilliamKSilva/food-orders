import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

class Restaurant(Base):
    __tablename__ = "restaurant"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[dict[str, any]]
    is_open: Mapped[bool]
    menu_items: Mapped[list["RestaurantMenuItem"]] = relationship(back_populates="restaurant")
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())

class RestaurantMenuItem(Base):
    __tablename__ = "restaurant_menu_item"
    id: Mapped[int] = mapped_column(primary_key=True)
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurant.id"))
    restaurant: Mapped["Restaurant"] = relationship(back_populates="menu_items")
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]
    available: Mapped[bool]
    order_items: Mapped[list["OrderItem"]] = relationship(back_populates="menu_item")
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
