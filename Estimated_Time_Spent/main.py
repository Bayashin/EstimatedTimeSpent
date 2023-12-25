import Estimated_Time_Spent.clustering as clustering
import Estimated_Time_Spent. graph as graph
import pandas as pd
import numpy as np

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
result_first = clustering.k_means_clustering(data_seconds_first, k, centroids)
result_end = clustering.k_means_clustering(data_seconds_end, k, centroids)

# 結果の出力
print(result_first)
for i, cluster in enumerate(result_first):
    centroid_time = cluster["centroid"]
    cluster_points = cluster["points"]
    
    print(f"Cluster {i + 1}: Centroid = {centroid_time}, Points = {cluster_points}")

# グラフの作成
graph.make_graph(result_first, "hayashiの入室時刻")
graph.make_graph(result_end, "hayashiの退室時刻")