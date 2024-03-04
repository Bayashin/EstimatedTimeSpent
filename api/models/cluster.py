from lib.mysql import Session
import models.struct as st

# userIdから最新のクラスタリングを取得する
def get_latest_cluster_by_userId(userId, reporting:bool):
    # DBセッションを取得
    session = Session()
    cluster = st.Cluster
    # clustersを取得
    cluster = session.query(cluster).filter(cluster.user_id == userId, cluster.reporting == reporting).order_by(cluster.date.desc()).first()
    return cluster

# 取得したclusterと同じuser_id、dateのclusterを全て取得する
def get_all_cluster_by_userId_and_date(userId, date, reporting:bool):
    # DBセッションを取得
    session = Session()
    cluster = st.Cluster
    # clustersを取得
    clusters = session.query(cluster).filter(cluster.user_id == userId, cluster.reporting == reporting, cluster.date == date).all()
    return clusters