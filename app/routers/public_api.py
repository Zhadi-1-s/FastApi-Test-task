from fastapi import APIRouter
from app.services.api_service import get_server_status, get_coin_data

router = APIRouter()

@router.get("/ping", summary="Check API server status")
async def ping():
    return await get_server_status()

@router.get("/coin/{coin_id}", summary="Get coin details by ID")
async def get_coin(coin_id: str):
    return await get_coin_data(coin_id)
