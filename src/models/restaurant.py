import datetime
from sqlalchemy import JSON, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

class Restaurant(Base):
    __tablename__ = "restaurant"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[dict[str, any]]
    menu_items: Mapped[str]
    is_open: Mapped[bool]
    created_at: Mapped[datetime.datetime]
    updated_at: Mapped[datetime.datetime]

class RestaurantMenuItem(Base):
    __tablename__ = "restaurant_menu_item"
    id: Mapped[int] = mapped_column(primary_key=True)
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurant.id"))
    restaurant: Mapped["Restaurant"] = relationship(back_populates="children")
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]
    avaiable: Mapped[bool]
    created_at: Mapped[datetime.datetime]
    updated_at: Mapped[datetime.datetime]
