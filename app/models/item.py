# app/models/item.py
from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # <- 自動生成
    name = Column(String, index=True)
    price = Column(Float)
