from __future__ import annotations
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from ..models import cluster as cl
from ..service import normal_distribution as nd
from ..lib.mysql import get_db

router = APIRouter()

# フロント側から現在の時刻を受け取ることとする（後で要変更)
# 今日のある時間までに特定のユーザーが入退室する確率、もしくはある時間以降に入退室する確率を返す
# 変数：user_id, true or false
@router.get("/app/probability/{reporting}/{before}")
async def get_probability_reporting_before(reporting:str, before:str, user_id:int = 0, str_date:str = "2024-1-1", time:str = "10:30:00", db: Session = Depends(get_db)):
    r = True if reporting == "reporting" else False
    b = True if before == "before" else False
    c = cl.get_latest_cluster_by_userId(db, user_id, r)
    date_object= datetime.strptime(str_date, '%Y-%m-%d')
    day = date_object.weekday()
    seven_days_ago= c.date - timedelta(days=6-day)
    clusters = cl.get_all_cluster_by_userId_and_date(db, user_id, seven_days_ago, r)
    delta = abs(clusters[0].date - cl.get_oldest_cluster_by_userId(db, user_id, r).date)
    # 差分を日単位に変換
    days_difference = delta.days
    # ここでクラスタリングの結果を元に確率を計算する(bがTrueなら以前, Falseなら以降)
    pr = nd.probability_from_normal_distribution(clusters, time, days_difference, b)
    return {"user_id": user_id, "probability": pr}

# # 時間より後にユーザーが入室する確率を返す
# @router.get("/app/probability/reporting/later")
# async def get_probability_reporting_later(user_id):
#     c = cl.get_latest_cluster_by_userId(user_id, True)
#     clusters = cl.get_all_cluster_by_userId_and_date(user_id, c.date, True)
#     # ここでクラスタリングの結果を元に確率を計算する
#     return {"user_id": user_id, "probability": 3.16}

# # 時間までにユーザーが退室する確率を返す
# @router.get("/app/probability/leaving/before")
# async def get_probability_leaving_before(user_id):
#     c = cl.get_latest_cluster_by_userId(user_id, False)
#     clusters = cl.get_all_cluster_by_userId_and_date(user_id, c.date, False)
#     # ここでクラスタリングの結果を元に確率を計算する
#     return {"user_id": user_id, "probability": 3.16}

# # 時間より後にユーザーが退室する確率を返す
# @router.get("/app/probability/leaving/later")
# async def get_probability_leaving_later(user_id):
#     c = cl.get_latest_cluster_by_userId(user_id, False)
#     clusters = cl.get_all_cluster_by_userId_and_date(user_id, c.date, False)
#     # ここでクラスタリングの結果を元に確率を計算する
#     return {"user_id": user_id, "probability": 3.16}