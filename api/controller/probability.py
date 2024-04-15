from __future__ import annotations
from typing import List
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from ..models import cluster as cl, user as us
from ..service import normal_distribution as nd
from ..lib.mysql import get_db

# レスポンス用のクラス
class ProbabilityResponse(BaseModel):
    userId: int
    userName: str
    probability: float

router = APIRouter()

# フロント側から現在の時刻を受け取ることとする（後で要変更)
# 今日のある時間までに特定のユーザーが入退室する確率、もしくはある時間以降に入退室する確率を返す
# 変数：user_id, true or false
@router.get("/app/probability/{reporting}/{before}" , response_class=ORJSONResponse, response_model=ProbabilityResponse)
async def get_probability_reporting_before(reporting:str, before:str, user_id:int = 0, date:str = "2024-1-1", time:str = "10:30:00", db: Session = Depends(get_db)):
    r = True if reporting == "reporting" else False
    b = True if before == "before" else False
    c = cl.get_latest_cluster_by_userId(db, user_id, r)
    date_object= datetime.strptime(date, '%Y-%m-%d')
    day = date_object.weekday()
    seven_days_ago= c.date - timedelta(days=6-day)
    clusters = cl.get_all_cluster_by_userId_and_date(db, user_id, seven_days_ago, r)
    delta = abs(clusters[0].date - cl.get_oldest_cluster_by_userId(db, user_id, r).date)
    # 差分を日単位に変換
    days_difference = delta.days
    # ここでクラスタリングの結果を元に確率を計算する(bがTrueなら以前, Falseなら以降)
    pr = nd.probability_from_normal_distribution(clusters, time, days_difference, b)
    result = ProbabilityResponse(userId=user_id, userName=us.get_user_by_id(db, user_id).name, probability=pr)
    return ORJSONResponse(result)

# 全てのユーザがその日に入室する確率を返す
@router.get("/app/probability/all/", response_class=ORJSONResponse, response_model=List[ProbabilityResponse])
async def get_probability_all(date:str = "2024-1-1", db: Session = Depends(get_db)):
    date_object= datetime.strptime(date, '%Y-%m-%d')
    day = date_object.weekday()
    seven_days_ago= date_object - timedelta(days=6-day)
    users = us.get_all_users(db)

    # 結果格納用のリスト
    result: list[ProbabilityResponse] = []

    # ユーザーごとに繰り返す
    for user in users:
        clusters = cl.get_all_cluster_by_userId_and_date(db, user.id, seven_days_ago, True)
        delta = abs(clusters[0].date - cl.get_oldest_cluster_by_userId(db, user.id, True).date)
        # 差分を日単位に変換
        days_difference = delta.days
        # ここでクラスタリングの結果を元に確率を計算する(bがTrueなら以前, Falseなら以降)
        pr = nd.probability_from_normal_distribution(clusters, "23:59:00", days_difference, True)
        result.append(ProbabilityResponse(userId=user.id, userName=user.name, probability=pr))

# resultをjsonに変換
    return ORJSONResponse(result)