import sqlite3

import aiosqlite
from database import queries


class AsyncDatabase:
    def __init__(self, db_path='db.sqlite3'):
        self.db_path = db_path

    async def create_tables(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(queries.CREAT_REVIEW_TABLE)
            await db.execute(queries.CREATE_FOOD_TABLE)
            await db.execute(queries.CREATE_CATEGORY_TABLE)
            await db.execute(queries.INSERT_CATEGORIES)
            await db.execute(queries.INSERT_FOOD)
            await db.commit()
            print("Database connected successfully")

    async def execute_query(self, query, params=None, fetch="none"):
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(query, params or ())

            if fetch == "none":
                await db.commit()
                return
            elif fetch == "all":
                data = await cursor.fetchall()
                return [dict(row) for row in data] if data else []
            elif fetch == 'one':
                data = await cursor.fetchone()
                return dict(data) if data else None