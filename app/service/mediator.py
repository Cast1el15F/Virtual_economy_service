from app.repository.postgresql.connect import ConnectPostgreSQL

class Mediator():
    Engine, SessionLocal = ConnectPostgreSQL.connect()