from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 接続したいDBへの接続情報
user_name = 'NAME'
password = 'PASSWORD'
host = "HOST"
port = "PORT"
database = "fastapi_sample"

engine = create_engine("mysql://{user_name}:{password}@{host}:{port}/{database}?charset=utf8")

SessionClass = sessionmaker(engine)
Session = SessionClass()