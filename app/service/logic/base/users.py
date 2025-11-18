from abc import ABC, abstractmethod

class UserAddFunds(ABC):
    """
    Пополнение баланса \n

    - Добавить валидацию суммы (> 0, макс. лимит) \n
    - Idempotency key для предотвращения дублирующих пополнений
    """

    @abstractmethod
    async def validate_amount(amount: float):
        pass

    @abstractmethod
    async def check_idempotency_key(key: str):
        pass

    @abstractmethod
    async def add_funds():
        pass

class UserGetInventory(ABC):
    """
    Получение инвентаря \n

    - Отдавать из кэша если возможно \n
    - Группировать consumable товары по quantity
    """

    @abstractmethod
    async def get_from_cache():
        pass

    @abstractmethod
    async def group_consumables():
        pass

    @abstractmethod
    async def get_inventory():
        pass