from typing import Annotated
from pydantic import Field
from app.service.entities.entity import *
from app.repository.postgresql.base.tables import *
from app.service.mediator import Mediator

class BD_tools():
    @staticmethod
    async def create_tables():
        Engine = Mediator.Engine
        async with Engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        return "All tables created successfully."
    
    @staticmethod
    async def drop_tables():
        Engine = Mediator.Engine
        async with Engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        return "All tables dropped successfully."
    
    @staticmethod
    async def add_user(user: User):
        SessionLocal = Mediator.SessionLocal
        async with SessionLocal() as session:
            async with session.begin():
                new_user = User(
                    username=user.username,
                    email=user.email,
                    balance=user.balance
                )
                session.add(new_user)
            await session.commit()
            return f"user {user.username} added successfully."

    @staticmethod
    async def add_product(product: Product):
        SessionLocal = Mediator.SessionLocal
        async with SessionLocal() as session:
            async with session.begin():
                new_product = Product(
                    name=product.name,
                    description=product.description,
                    price=product.price,
                    type=product.type,
                    is_active=product.is_active
                )
                session.add(new_product)
            await session.commit()
            return f"product {product.name} added successfully."

    @staticmethod
    async def add_product(product: Product):
        SessionLocal = Mediator.SessionLocal
        async with SessionLocal() as session:
            async with session.begin():
                new_product = Product(
                    name=product.name,
                    description=product.description,
                    price=product.price,
                    type=product.type,
                    is_active=product.is_active
                )
                session.add(new_product)
            await session.commit()
            return f"product {product.name} added successfully."
