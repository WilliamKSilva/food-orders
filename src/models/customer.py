import datetime
from sqlalchemy.orm import mapped_column, Mapped

from models.base import Base

class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    phone_number: Mapped[str]
    default_address: Mapped[dict[str, any]]
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())