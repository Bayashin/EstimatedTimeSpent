import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from datetime import datetime
import matplotlib.dates as mdates

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

def make_graph(clusters):
    # データを日時オブジェクトに変換
    data = [datetime.strptime(time, "%H:%M:%S.%f") if '.' in time else datetime.strptime(time, "%H:%M:%S") for time in time_data]

    # クラスタのデータを日時オブジェクトに変換（ミリ秒を含む）
    cluster_data = {cluster['centroid']: [datetime.strptime(time, "%H:%M:%S.%f") if '.' in time else datetime.strptime(time, "%H:%M:%S") for time in cluster['points']] for cluster in clusters}

    # グラフの作成
    fig, ax = plt.subplots(figsize=(12, 6))
    for cluster, times in cluster_data.items():
        ax.scatter(times, [1] * len(times), label=f"Cluster {list(cluster_data.keys()).index(cluster) + 1}")

# クラスタのセントロイドをプロット
    for cluster in clusters:
        centroid_time = datetime.strptime(cluster['centroid'], "%H:%M:%S")
        ax.scatter(centroid_time, 1, c='black', marker='x', s=100, label=f"Centroid {clusters.index(cluster) + 1} ")

# グラフの設定
    ax.yaxis.set_visible(False)  # y軸を非表示にする
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # x軸のフォーマットを設定
    plt.xlabel('時間')
    plt.title('hayashiの入室した時間')
    plt.legend()

    # グラフを表示
    plt.show()

# 入力データのパース
time_data = [
    "08:11:41.859", "08:22:22.226", "08:46:37.590", "08:46:01.208", "08:36:44.679",
    "08:40:49.586", "08:46:28.548", "09:59:28.740", "08:35:32.321", "10:22:07.852",
    "08:33:45.183", "08:07:22.920", "08:34:16.666", "08:40:08.239", "09:10:07.362",
    "08:29:42.010", "08:24:35.053", "08:34:03.306", "08:38:46.798", "08:45:19.724",
    "08:26:56.303", "08:18:04.055", "08:19:08.538", "08:25:08.055", "15:32:34.266",
    "08:33:10.705", "08:25:39.100", "08:29:43.298", "08:29:08.290", "08:33:43.808",
    "08:32:04.731"
]


# 時間データを秒単位に変換
data_seconds = np.array([sum(x * float(t) for x, t in zip([3600, 60, 1], point.split(":"))) for point in time_data])

# クラスタリングの実行
k = 3  # クラスタの数
# 初期値を設定
initial_centroids = ["6:00", "12:00", "18:00"]
# 初期値を秒単位に変換
centroids = np.array([sum(x * int(t) for x, t in zip([3600, 60], point.split(":"))) for point in initial_centroids])
result = k_means_clustering(data_seconds, k, centroids)

# 結果の出力
print(result)
for i, cluster in enumerate(result):
    centroid_time = cluster["centroid"]
    cluster_points = cluster["points"]
    
    print(f"Cluster {i + 1}: Centroid = {centroid_time}, Points = {cluster_points}")

# グラフの作成
make_graph(result)