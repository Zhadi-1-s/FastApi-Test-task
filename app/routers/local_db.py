from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/coins", response_model=schemas.Coin, summary="Add a new coin")
def create_coin(coin: schemas.CoinCreate, db: Session = Depends(get_db)):
    db_coin = models.CoinData(**coin.dict())
    db.add(db_coin)
    db.commit()
    db.refresh(db_coin)
    return db_coin

@router.get("/coins/{coin_id}", response_model=schemas.Coin, summary="Get coin by ID")
def read_coin(coin_id: int, db: Session = Depends(get_db)):
    db_coin = db.query(models.CoinData).filter(models.CoinData.id == coin_id).first()
    if db_coin is None:
        raise HTTPException(status_code=404, detail="Coin not found")
    return db_coin
