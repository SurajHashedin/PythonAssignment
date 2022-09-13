from datetime import datetime
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, Union

class DataTracker(BaseModel):
    id: Optional[UUID] = uuid4
    username: str 
    key: str
    value: str
    datatype: str
    tags: str 
    createdAt: Union[datetime,None] = None
    updatedAt: Union[datetime,None] = None 
