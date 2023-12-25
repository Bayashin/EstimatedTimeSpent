import numpy as np
import pandas as pd
from datetime import datetime

def convert_seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

def k_means_clustering(data, k, centroids):
    
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
    
    return clusters