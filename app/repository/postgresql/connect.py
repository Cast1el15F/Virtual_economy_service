from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.repository.config import CONFIG


class ConnectPostgreSQL:
    """Класс для подключения к PostgreSQL через SQLAlchemy async.
    connect() возвращает фабрику асинхронных сессий (async_sessionmaker).
    """

    @staticmethod
    def connect():
        engine = create_async_engine(
            CONFIG.DATABASE_URL,
            echo=True,
            future=True,
        )

        SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
        return SessionLocal