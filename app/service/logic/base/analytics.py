from abc import ABC, abstractmethod

class GetPopularProducts(ABC):
    """
    Аналитика популярных товаров \n

    - Топ-5 товаров по количеству покупок за последние 7 дней \n
    - Кэшировать на 1 час \n
    """

    @abstractmethod
    async def get_popular_products():
        pass
