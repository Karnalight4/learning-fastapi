from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings


while True:
    try:
        # remove this line if I want to only use alembic 
        # this is will create the table in the database on the app start 
        # could remove it it use alembic to add the table to the database
        models.Base.metadata.create_all(bind=engine)
        print("\tDatabase connection was succesfull.")
        break
    
    except Exception as error:
        print("Connecting to database failed.")
        print("ERROR: ", error)
        time.sleep(5)

app = FastAPI()

origin = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


