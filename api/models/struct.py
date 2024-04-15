from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)
# datetime型をインポート
import datetime

# sqlalchemyのモデルを作成する
# Baseクラスを作成
class Base(DeclarativeBase):
    pass

# Baseクラスを継承したモデルを作成
# # usersテーブルのモデルUsers
# class Users(Base):
#     __tablename__ = 'users'
#     user_id = mapped_column(Integer, primary_key=True, autoincrement=True)
#     uid = mapped_column(String(255), nullable=False)
#     name = mapped_column(String(255), nullable=False)
#     email = mapped_column(String(255), nullable=False)
#     role = mapped_column(String(255), nullable=False)
# logs(仮)テーブルのモデルLogs(仮)
class Logs(Base):
    __tablename__ = 'edited_logs'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    date:Mapped[datetime.date] = mapped_column(nullable=False)
    Reporting:Mapped[datetime.time] = mapped_column(nullable=False)
    Leave:Mapped[datetime.time] = mapped_column(nullable=False)
# clusterテーブルのモデルCluster
class Cluster(Base):
    __tablename__ = 'clusters'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    date: Mapped[datetime.date] = mapped_column(nullable=False)
    reporting: Mapped[bool]
    average: Mapped[float] = mapped_column(nullable=False)
    sd: Mapped[float] = mapped_column(nullable=False)
    count: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(nullable=False)