import datetime
from sqlalchemy import TIMESTAMP 
from sqlalchemy.dialects.postgresql import JSONB 
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    type_annotation_map = {
        dict[str, any]: JSONB,
        datetime.datetime: TIMESTAMP(timezone=True)
    }