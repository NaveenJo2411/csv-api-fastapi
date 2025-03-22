from fastapi import FastAPI,Query
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import csv

data = []

@asynccontextmanager
async def lifespan(app: FastAPI):
    global data
    with open("second_hlf.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    yield  # App starts here
    # Optional: Cleanup code can go after yield

app = FastAPI(lifespan=lifespan)

@app.get("/records")
def get_records(skip: int = 0, limit: int = 10):
    # return JSONResponse(content=data[skip: skip + limit])
    total = len(data)
    return{
        "data" : data[skip: skip + limit],
        "total" : total,
        "skip"  : skip,
        "limit" : limit 
    }