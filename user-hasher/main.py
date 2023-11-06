import hashlib
import logging
import os
import time

from fastapi import FastAPI, Header, Request, Response
from aioprometheus import REGISTRY, Counter, render, Histogram


from typing import List


# Instantiate the app
app = FastAPI()

# Setup logging
logger = logging.getLogger("uvicorn.error")

graphs = {}
graphs['c'] = Counter('Req operation total', 'total number of processed req')
graphs['h'] = Histogram('Req duration', 'Histogram for duration is sec', buckets=(.1,.5,1,2,3,5))
# Load and log APP_VERSION
APP_VERSION = os.environ.get("APP_VERSION", "production")
logger.info(f"APP_VERSION={APP_VERSION}")


@app.get("/version")
async def version():
    return {"version": APP_VERSION}


@app.get("/user_hash")
async def user_hash(user_id: str):
    start = time.time()
    graphs['c'].inc()
    hash = hashlib.sha1(
        (user_id + os.environ.get("USER_SALT", "")).encode()
    ).hexdigest()
    end = time.time()
    graphs['h'].observe(end - start)
    return hash
    


@app.get("/metrics")
async def request_count():
    res =[]
    for k,v in graphs.items():
        res.append()
        return Response(res, mimetype="text/plain")