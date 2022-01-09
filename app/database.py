import time
import sqlalchemy
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:' \
                          f'{settings.db_port}/{settings.db_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()  # type: sqlalchemy.orm.Session
    try:
        yield db
    finally:
        db.close()

# manual connection without using sqalchemy
# while True:
#
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='postgres21',
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database Connection Successful")
#         break
#     except Exception as error:
#         print("Connection to DB failed")
#         print("Error: ", error)
#         time.sleep(2)
