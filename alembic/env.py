import asyncio
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine # Добавляем импорт AsyncEngine для типизации

from alembic import context

# Это важно: импортируйте ваш асинхронный движок и базовый класс моделей
# Убедитесь, что 'app.database' указывает на ваш database.py
from app.database import async_engine, Base, url_database

# Это ваш target_metadata, который Alembic будет использовать для автогенерации
# Все ваши модели должны наследовать от этого Base
target_metadata = Base.metadata

# Прочие настройки из alembic.ini
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired here.
# ...

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is additionally
    passed api. The key thing is to prevent
    actual database connections being made, since
    don't expect to be in a DB-connected environment
    to run after all.

    """
    url = url_database # Используем вашу URL из database.py
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # Вместо создания нового engine, используем существующий async_engine
    connectable: AsyncEngine = async_engine

    # Теперь мы должны асинхронно получить соединение и передать его Alembic
    async with connectable.connect() as connection:
        # connection.run_sync() позволяет выполнять синхронные функции
        # в асинхронном контексте, что необходимо для Alembic.
        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    # Здесь мы запускаем асинхронную функцию в синхронном контексте
    asyncio.run(run_migrations_online())