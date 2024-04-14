from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 接続したいDBへの接続情報
user_name = 'NAME'
password = 'PASSWORD'
host = "HOST"
port = "PORT"
database = "fastapi_sample"

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://{user_name}:{password}@{host}:{port}/{database}?charset=utf8"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()