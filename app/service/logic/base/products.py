from abc import ABC, abstractmethod

class Purchase_product(ABC):
    """
    Покупка товара \n
    
    - Проверка баланса пользователя \n
    - Atomic transaction: списание средств + запись в инвентарь + запись транзакции \n
    - Для consumable товаров увеличивать quantity, для permanent — проверять дубликаты \n
    - Кэширование: кэшировать инвентарь пользователя на 5 минут
    """

    @abstractmethod
    async def purchase(product_id: int):
        pass

class Use_product(ABC):
    """
    Использование consumable товара \n

    - Уменьшение quantity в инвентаре \n
    - Проверка, что товар доступен у пользователя
    """

    @abstractmethod
    async def use(product_id: int):
        pass