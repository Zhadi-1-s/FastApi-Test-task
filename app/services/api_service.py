import httpx
from fastapi import HTTPException

BASE_URL = "https://api.coingecko.com/api/v3"

async def get_server_status():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/ping")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch server status")
        return response.json()

async def get_coin_data(coin_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/coins/{coin_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Coin not found")
        return response.json()
