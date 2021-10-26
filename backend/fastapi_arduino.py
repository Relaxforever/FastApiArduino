#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI
import logging
from fastapi.middleware.cors import CORSMiddleware
import csv
#from random import randrange
from pydantic import BaseModel


#header = ['temp',  'distance']

class DataTempDistance(BaseModel):
    temp: float
    distance: int



app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
    "*"
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
async def arduino(request: DataTempDistance):
    with open('arduino_data.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        #print(request)
        data = [request.temp, request.distance]
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
                data_object.append(DataTempDistance(row[0], row[1]))
                line_count += 1
    print(f'Processed {line_count} lines')

    return {"body": data_object}

if __name__ == "__main__":

    uvicorn.run("fastapi_arduino:app", host="127.0.0.1",
                port=4000, log_level="info")
