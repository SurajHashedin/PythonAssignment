from datetime import datetime
from http.client import HTTPException
from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import DataTracker,updateDataTracker

# create an app object
app = FastAPI()

# updated dummy data
db: List[DataTracker] = [ \
    DataTracker( \
    id = uuid4(), \
    username = 'test', \
    key = 'keytest', \
    value = 'valuetest', \
    datatype = 'datatypetest', \
    tags = 'tagstest', \
    createdAt = datetime.now(), \
    updatedAt = datetime.now()
 )]


#fetching all metrics records 
@app.get("/api/v1/metrics")
async def fetch_metrics():
    return db 

#Add metrics records 
@app.post("/api/v1/metrics")
async def create_metrics(datatracker: DataTracker):
    datatracker.createdAt = datetime.now()
    datatracker.updatedAt = datetime.now()
    db.append(datatracker)
    return {'id': datatracker.id}

#delete metrics records 
@app.delete("/api/v1/metrics/{username}")
async def delete_username(username:str):
    for data in db:
        if data.username == username:
            db.remove(data)
            return 'deleted'
    raise HTTPException(
        status_code = 404,
        detail = f"{username} is deleted"
    )

#update metrics records 
@app.put("/api/v1/metrics/{data}")
async def update_data(data_update: updateDataTracker, data:str):
    for dt in db:
        if dt.username == data:
            if data_update.key is not None:
                dt.key = data_update.key
            if data_update.value is not None:
                dt.value = data_update.value
            if data_update.datatype is not None:
                dt.datatype = data_update.datatype
            if data_update.tags is not None:
                dt.tags = data_update.tags

            dt.updatedAt = datetime.now()
            return 'Updated'
    raise HTTPException(
        status_code = 404,
        detail = f"{data} is deleted"
    )