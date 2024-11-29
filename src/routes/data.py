from fastapi import FastAPI, APIRouter, Depends, Request
from helpers.config import get_settings, Settings
from models.ContactModel import ContactModel

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1"]
)
settings = get_settings()


@data_router.post("/upload")
async def upload_data(request: Request):
    _ = await ContactModel.insert_contact(request.app.db_client)


