from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.repository.config import CONFIG
from app.service.exceptions.postgre_exceptions import *


class ConnectPostgreSQL:
    """Класс для подключения к PostgreSQL через SQLAlchemy async.
    connect() возвращает кортеж `(engine, async_sessionmaker)`.
    Engine необходим для выполнения DDL через `engine.begin()` + `conn.run_sync(...)`.
    """

    @staticmethod
    def connect():
        try:
            Engine = create_async_engine(
                CONFIG.DATABASE_URL,
                echo=True,
                future=True,
            )
        except:
            raise EngineCreatePostgreSQLError

        try:
            SessionLocal = async_sessionmaker(bind=Engine, expire_on_commit=False)
        except:
            raise SessionLocalCreatePostgreSQLError

        
        return Engine, SessionLocal