from pydantic import BaseModel

class CoinCreate(BaseModel):
    name: str
    symbol: str
    price: str | None = None

class Coin(CoinCreate):
    id: int

    class Config:
        orm_mode = True
