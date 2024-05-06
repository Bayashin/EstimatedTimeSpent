from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 接続したいDBへの接続情報
user_name = 'root'
password = 'admin'
host = '127.0.0.1'
port = '3309'
database = 'testdb'

SQLALCHEMY_DATABASE_URL = "mysql://" + user_name + ":" + password + "@" + host + ":" +port + "/" + database + "?charset=utf8&unix_socket=/var/run/mysqld/mysqld.sock"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()