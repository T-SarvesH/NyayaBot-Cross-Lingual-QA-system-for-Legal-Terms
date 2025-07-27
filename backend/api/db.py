import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from contextlib import asynccontextmanager

load_dotenv()

MONGODB_URL = os.getenv("MONGO_URL")

@asynccontextmanager
async def lifespan(app: FastAPI):

    """ Creating a Mongo client to access the cluster and database"""

    app.state.mongo_client = AsyncIOMotorClient(MONGODB_URL)
    app.state.db = app.state.mongo_client["Nyayabot"]

    try:
        yield
    finally:
        app.state.mongo_client.close()

# Dependency injection which returns db instance at each request
def get_db(app: FastAPI):
    return app.state.db