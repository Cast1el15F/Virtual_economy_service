from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ConnectPostgreSQL:
    """Класс для подключения к PostgreSQL через SQLAlchemy. \n
    connect() возвращает фабрику сессий."""

    async def connect(self):
        engine = create_engine(
            "postgresql+psycopg://myuser:secret@localhost:5432/mydb",
            echo=True,        # включаем логи SQL (удобно на dev)
            future=True       # обязательный флаг для 2.0+
        )

        # Фабрика сессий
        SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
        return SessionLocal