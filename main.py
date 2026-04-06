from fastapi import FastAPI
import models
from database import engine, Base

from routes import users,records,dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Dashboard API")

app.include_router(users.router)
app.include_router(records.router)
app.include_router(dashboard.router)