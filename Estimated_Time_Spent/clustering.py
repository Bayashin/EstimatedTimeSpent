import numpy as np
import pandas as pd
from datetime import datetime

def convert_seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

def k_means_clustering(data, k):
    # ランダムな点をk個設置
    centroids = np.random.choice(data, size=k, replace=False)
    
    while True:
        # ステップ2: 最も近い点が同じデータでグループ化
        groups = [[] for _ in range(k)]
        for point in data:
            distances = [np.linalg.norm(point - np.array(centroid)) for centroid in centroids]
            closest_centroid_index = np.argmin(distances)
            groups[closest_centroid_index].append(point)
        
        # ステップ3: グループごとの平均を求めてそれを新たな点とする
        new_centroids = [np.mean(group, axis=0) for group in groups]
        
        # ステップ5: 新しい中心点が以前の中心点と同じであれば終了
        if np.array_equal(centroids, new_centroids):
            break
        
        centroids = new_centroids
    
    # ステップ6: クラスタリングした結果を出力
    clusters = []
    for i, group in enumerate(groups):
        centroid_time = convert_seconds_to_hms(int(centroids[i]))
        cluster_points = [convert_seconds_to_hms(point) for point in group]
        
        clusters.append({
            "centroid": centroid_time,
            "points": cluster_points
        })
    # print(clusters)
    return clusters

def xmeans(data):
    # 初期クラスタ数
    k = 1
    
    while True:
        # K-means法でクラスタリング
        clusters = k_means_clustering(data, k)
        # for i, cluster in enumerate(clusters):
        #     centroid_time = cluster["centroid"]
        #     cluster_points = cluster["points"]
        #     print(f"Cluster {i + 1}: Centroid = {centroid_time}, Points = {cluster_points}")

        # クラスタごとにデータポイントを秒に変換
        data_seconds = [[sum(x * int(t) for x, t in zip([3600, 60, 1], point.split(":"))) for point in cluster['points']] for cluster in clusters]
        # print(data_seconds)

        # クラスタごとにデータ分散を計算
        cluster_variances = [np.var(cluster_data) for cluster_data in data_seconds]

        # クラスタ内のデータ分散の平均を計算
        avg_cluster_variance = np.mean(cluster_variances)
        
        # print(cluster_variances)
        # print(f"クラスタ数: {k}, クラスタ内のデータ分散の平均: {avg_cluster_variance}")
        print("")
        
        # クラスタ内のデータ分散が閾値以下なら終了
        if avg_cluster_variance < 35000000:
            break
        
        # クラスタ数を増やして再実行
        k += 1

    return clusters