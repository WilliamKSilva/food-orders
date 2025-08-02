import datetime
from sqlalchemy.orm import mapped_column, Mapped

from models.base import Base

class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str]
    default_address: Mapped[dict[str, any]]
    created_at: Mapped[datetime.datetime]
    updated_at: Mapped[datetime.datetime]