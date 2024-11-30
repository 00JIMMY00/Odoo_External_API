from pydantic import BaseModel
from typing import Optional


class ProcessRequest(BaseModel):
    name: str
    email: Optional[str] = None
