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
    async def check_balance():
        pass

    @abstractmethod
    async def process_transaction():
        pass

    @abstractmethod
    async def add_quantity_for_consumable():
        pass

    @abstractmethod
    async def check_for_duplicates():
        pass

    @abstractmethod
    async def cache():
        pass

    @abstractmethod
    async def purchase():
        pass

class Use_consumable_product(ABC):
    """
    Использование consumable товара \n

    - Уменьшение quantity в инвентаре \n
    - Проверка, что товар доступен у пользователя
    """

    @abstractmethod
    async def check_availability():
        pass

    @abstractmethod
    async def decrease_quantity():
        pass

    @abstractmethod
    async def use():
        pass