from fastapi import FastAPI
from app.service.entities.entity import *
from app.api.routers import *
import test

app = FastAPI(
    title="Virtual Economy Service API",
    docs_url="/api/docs",
)

# @app.post("/products/{product_id}/purchase")
# async def purchase_product(product_id: int):
#     """
#     Покупка товара \n
    
#     - Проверка баланса пользователя \n
#     - Atomic transaction: списание средств + запись в инвентарь + запись транзакции \n
#     - Для consumable товаров увеличивать quantity, для permanent — проверять дубликаты \n
#     - Кэширование: кэшировать инвентарь пользователя на 5 минут
#     """
#     pass

@app.get("/root")
async def read_root():
    t = await test.read_root()
    return t


# uvicorn app.api.main:app --reload