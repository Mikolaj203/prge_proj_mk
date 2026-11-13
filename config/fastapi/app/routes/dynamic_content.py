import os
from fastapi import APIRouter
from sqlalchemy import create_engine, text

db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")

# Utwórz silnik raz globalnie
db_connection = create_engine(f'postgresql://{db_user}:{db_password}@postgis:5432/{db_name}')

router_get_users_from_database = APIRouter()

@router_get_users_from_database.get("/users_db")
async def get_users():
    try:
        sql_query = text('SELECT * FROM public.users;')
        with db_connection.connect() as connection:
            result = connection.execute(sql_query)
            users = [dict(row._mapping) for row in result]
        return users
    except Exception as e:
        return {'error': str(e)}