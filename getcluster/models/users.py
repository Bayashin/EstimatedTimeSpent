from __future__ import annotations
from sqlalchemy.orm import Session
from . import struct as st

# userを全て取得
def get_all_users(db: Session) -> list[st.Users]:
    # usersを取得
    users = db.query(st.Users).all()
    return users