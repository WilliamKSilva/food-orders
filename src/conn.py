import os

import models.customer
import models.order
import models.restaurant

from sqlalchemy import create_engine, Engine
from models.base import Base

def initDB() -> Engine: 
    try:
        DB_NAME = os.getenv("DB_NAME")
        DB_PORT = os.getenv("DB_PORT")
        DB_HOST = os.getenv("DB_HOST")
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")

        engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)

        Base.metadata.create_all(engine)
    except Exception as err:
        print(f"[INFO] error trying to connect to database: {err}")
        exit()

    return engine
