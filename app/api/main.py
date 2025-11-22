from fastapi import FastAPI
from app.service.entities.entity import *
from app.api.routers import *
from app.service.logic.bd_tools import BD_tools
import test

app = FastAPI(
    title="Virtual Economy Service API",
    docs_url="/api/docs",
)

@app.post("/create_tables/")
async def add_user():
    return await BD_tools.create_tables()

@app.post("/drop_tables/")
async def add_user():
    return await BD_tools.drop_tables()

@app.post("/add_user/")
async def add_user(user: User):
    return await BD_tools.add_user(user)

@app.post("/add_product/")
async def add_user(product: Product):
    return await BD_tools.add_product(product)


# uvicorn app.api.main:app --reload