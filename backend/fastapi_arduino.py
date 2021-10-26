#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI, Request
import logging
from fastapi.middleware.cors import CORSMiddleware
import csv
#from random import randrange
from pydantic import BaseModel


#header = ['temp',  'distance']

class data_temp_distance:
    def __init__(self, temp, distance):
        self.temp = temp
        self.distance = distance

    class Config:
        schema_extra = {
            "temp": 32,
            "distance": 10
        }


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


@app.post('/api/arduino', summary="", description="", items=data_temp_distance)
async def arduino(request: Request):
    with open('arduino_data.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        data = [Request.temp, Request.distance]
        print(data)
        writer.writerow(data)
    print("Arduino")
    pass


@app.get("/todo", tags=["todos"])
async def get_temperature():
    with open('arduino_data.csv', 'r', encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        line_count = 0
        data_object = []

        for row in csv_reader:
            if line_count == 0:
                print(f'las columnas actuales son {", ".join(row)}')
                line_count += 1
            else:
                data_object.append(data_temp_distance(row[0], row[1]))
                line_count += 1
    print(f'Processed {line_count} lines')

    return {"body": data_object}

if __name__ == "__main__":

    uvicorn.run("fastapi_arduino:app", host="127.0.0.1",
                port=4000, log_level="info")
