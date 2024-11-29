from fastapi import FastAPI, APIRouter, Depends, Request
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def welcome(request:Request , app_settings: Settings=Depends(get_settings)):
    app_settings = get_settings()

    db_name = app_settings.DB_NAME
    user_name = app_settings.USERNAME
    return{
        "app_name":db_name,
        "app_version":user_name
    }