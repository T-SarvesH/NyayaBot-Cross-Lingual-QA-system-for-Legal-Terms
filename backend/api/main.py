from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import get_db, lifespan
from motor.motor_asyncio import AsyncIOMotorDatabase    

app = FastAPI(title="NyayabotApp", lifespan=lifespan)

""" React at lochost 5173 """

allowed_hosts = [

    "http://localhost:5173",

    #Backup React port
    "http://localhost:5174",
    
    "http://localhost:3000",
    "http://localhost:3001",
    
]

app.add_middleware(

    CORSMiddleware,
    allow_origins = allowed_hosts,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
async def root(db: AsyncIOMotorDatabase = get_db(app)):
    return {"Message": "Welcome to Nyayabot"}

@app.post("/query")
async def queryHandle(db: AsyncIOMotorDatabase = get_db(app)):
    pass

# For more info visit lochost 8801/docs for all methods info