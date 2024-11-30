from fastapi import FastAPI, APIRouter, Depends, Request, status
from helpers.config import get_settings, Settings
from models.ContactModel import ContactModel
from .schemes.data import ProcessRequest
from .enums import ResponseSignal
from fastapi.responses import JSONResponse


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1"]
)
settings = get_settings()


@data_router.post("/upload")
async def upload_data(request: Request, process_request : ProcessRequest):

    myData = process_request.model_dump(by_alias=True, exclude_unset=True)
    try:
        _ = await ContactModel.insert_contact(request.app.db_client, myData=myData)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "signal":ResponseSignal.DATA_INSERTION_SUCCESS.value
            }
        )
    
    except Exception as e :
        print(f"Failed to connect to Odoo API: {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal":ResponseSignal.DATA_INSERTION_FAILED.value
            }
        )
        


    


