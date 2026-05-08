from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    count = Column(Integer, nullable=False)
    # Задание 9.1 (часть 6): Добавлено новое поле NOT NULL
    description = Column(String, nullable=False, default="Описание отсутствует")