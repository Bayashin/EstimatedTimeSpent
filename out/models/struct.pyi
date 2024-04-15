import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped as Mapped

class Base(DeclarativeBase): ...

class Logs(Base):
    __tablename__: str
    id: Mapped[int]
    user_id: Mapped[int]
    date: Mapped[datetime.date]
    Reporting: Mapped[datetime.time]
    Leave: Mapped[datetime.time]

class Cluster(Base):
    __tablename__: str
    id: Mapped[int]
    date: Mapped[datetime.date]
    reporting: Mapped[bool]
    average: Mapped[float]
    sd: Mapped[float]
    count: Mapped[int]
    user_id: Mapped[int]
