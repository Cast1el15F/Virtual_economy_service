from fastapi import FastAPI
from app.service.entities.entity import *

app = FastAPI(
    title="Virtual Economy Service API"
)

@app.post("/products/{product_id}/purchase")
async def purchase_product(product_id: int):
    """
    Покупка товара \n
    
    - Проверка баланса пользователя \n
    - Atomic transaction: списание средств + запись в инвентарь + запись транзакции \n
    - Для consumable товаров увеличивать quantity, для permanent — проверять дубликаты \n
    - Кэширование: кэшировать инвентарь пользователя на 5 минут
    """
    pass