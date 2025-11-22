class EngineCreatePostgreSQLError(Exception):
    def __str__(self):
        return "Ошибка создания engine для подключения к PostgreSQL."

class SessionLocalCreatePostgreSQLError(Exception):
    def __str__(self):
        return "Ошибка создания SessionLocal для подключения к PostgreSQL."