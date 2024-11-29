from fastapi import FastAPI, HTTPException
from helpers.config import get_settings, Settings
import xmlrpc.client
from routes import base, data
app = FastAPI()


# Load settings
settings = get_settings()

# Define XML-RPC client globally
# models = None

@app.on_event("startup")
async def startup():
    """
    Initialize the XML-RPC connection on startup.
    """
    # global models
    try:
        app.db_client = xmlrpc.client.ServerProxy(f"{settings.URL}/xmlrpc/2/object")
        print("Connected to Odoo API")
    except Exception as e:
        print(f"Failed to connect to Odoo API: {e}")
        raise HTTPException(status_code=500, detail="Failed to connect to Odoo API")

# Include API routes
app.include_router(base.base_router)
app.include_router(data.data_router)