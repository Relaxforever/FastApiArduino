#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI, Request
import logging
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

Temp_Data = [
    {
        "temp": 32,
        "distance": 15
    },
    {
        "temp": 33,
        "distance": 15
    },
    {
        "temp": 32.3,
        "distance": 10
    },
    {
        "temp": 32.3,
        "distance": 10
    },
    {
        "temp": 32.3,
        "distance": 10
    }
]

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
app = FastAPI(title="Arduino FastAPI",
              description="Here's our API...", version="1.0")


@app.post('/api/arduino', summary="", description="")
async def arduino(request: Request):
    print("Arduino")
    pass


@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    return {"data": Temp_Data}

if __name__ == "__main__":

    uvicorn.run("fastapi_arduino:app", host="127.0.0.1",
                port=4000, log_level="info")
