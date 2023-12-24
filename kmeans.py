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

# CSVファイルからデータを読み込む
file_path = 'processed_data/hayashi_09-10.csv'  # ファイルパスを適切に設定
df = pd.read_csv(file_path, delimiter=',')  # タブ区切りの場合
# 時間の文字列をdatetime型に変換
df_entry = df['first_entry'].to_list()
df_exit = df['last_exit'].to_list()

# 時間データを秒単位に変換
data_seconds_first = np.array([sum(x * float(t) for x, t in zip([3600, 60, 1], point.split(":"))) for point in df_entry])
data_seconds_end   = np.array([sum(x * float(t) for x, t in zip([3600, 60, 1], point.split(":"))) for point in df_exit])

# クラスタリングの実行
k = 3  # クラスタの数
# 初期値を設定
initial_centroids = ["6:00", "12:00", "18:00"]
# 初期値を秒単位に変換
centroids = np.array([sum(x * int(t) for x, t in zip([3600, 60], point.split(":"))) for point in initial_centroids])
result_first = k_means_clustering(data_seconds_first, k, centroids)
result_end = k_means_clustering(data_seconds_end, k, centroids)

# 結果の出力
print(result_first)
for i, cluster in enumerate(result_first):
    centroid_time = cluster["centroid"]
    cluster_points = cluster["points"]
    
    print(f"Cluster {i + 1}: Centroid = {centroid_time}, Points = {cluster_points}")