from fastapi import APIRouter
import api.models.cluster as cl

router = APIRouter()

# 時間までにユーザーが入室する確率を返す
# 変数：user_id, true or false
@router.get("/app/probability/{reporting}/{before}")
async def get_probability_reporting_before(reporting:str, before:str, user_id:int = 0):
    r = True if reporting == "reporting" else False
    b = True if before == "before" else False
    c = cl.get_latest_cluster_by_userId(user_id, r)
    clusters = cl.get_all_cluster_by_userId_and_date(user_id, c.date, r)
    # ここでクラスタリングの結果を元に確率を計算する(bがTrueなら以前, Falseなら以降)
    return {"user_id": user_id, "probability": 3.16}

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