#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI, Request
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
app = FastAPI(title="Arduino FastAPI", description="Here's our API...", version="1.0")

@app.post('/api/arduino', summary="", description="")

async def arduino(request: Request):
    pass

if __name__ == "main":
    uvicorn.run("fastapi_arduino:app", host="127.0.0.1", port=4000, log_level="info")