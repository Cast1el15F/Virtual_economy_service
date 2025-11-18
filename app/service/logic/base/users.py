from abc import ABC, abstractmethod

class UserAddFunds(ABC):
    """
    Пополнение баланса \n

    - Добавить валидацию суммы (> 0, макс. лимит) \n
    - Idempotency key для предотвращения дублирующих пополнений
    """

    @abstractmethod
    async def add_funds(user_id: int, amount: float):
        pass

class UserGetInventory(ABC):
    """
    Получение инвентаря \n
    - Отдавать из кэша если возможно \n
    - Группировать consumable товары по quantity
    """

    @abstractmethod
    async def get_inventory(user_id: int):
        pass