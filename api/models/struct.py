# sqlalchemyライブラリから使用する型などをインポート
from sqlalchemy import Column, Integer, Float , Date, Time, Boolean
# Baseクラス作成用にインポート
from sqlalchemy.ext.declarative import declarative_base

# Baseクラスを作成
Base = declarative_base()

# Baseクラスを継承したモデルを作成
# # usersテーブルのモデルUsers
# class Users(Base):
#     __tablename__ = 'users'
#     user_id = Column(Integer, primary_key=True, autoincrement=True)
#     uid = Column(String(255), nullable=False)
#     name = Column(String(255), nullable=False)
#     email = Column(String(255), nullable=False)
#     role = Column(String(255), nullable=False)
# logs(仮)テーブルのモデルLogs(仮)
class Logs(Base):
    __tablename__ = 'logs'
    log_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    Reporting = Column(Time, nullable=False)
    Leave = Column(Time, nullable=False)
# clusterテーブルのモデルCluster
class Cluster(Base):
    __tablename__ = 'cluster'
    cluster_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    reporting = Column(Boolean, nullable=False)
    average = Column(Float, nullable=False)
    sd = Column(Float, nullable=False)
    user_id = Column(Integer, nullable=False)