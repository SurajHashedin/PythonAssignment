from datetime import datetime
from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import DataTracker

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
    createdAt= datetime.now(), \
    updatedAt= datetime.now() )]

#fetching all metrics records 
@app.get("/api/v1/metrics")
async def fetch_metrics():
    return db 