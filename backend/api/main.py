from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Nyayabot")

""" React at lochost 5173 """
allowed_hosts = [

    "http://localhost:5173",

    #Backup port
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
async def root():
    return {"Message": "Welcome to Nyayabot"}

#For more info visit lochost 8801/docs for all methods info