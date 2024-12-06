from sqlalchemy import Column, Integer, String
from app.database import Base

class CoinData(Base):
    __tablename__ = "coin_data"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    symbol = Column(String, index=True)
    price = Column(String, nullable=True)
