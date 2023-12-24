import matplotlib.pyplot as plt
import japanize_matplotlib
import matplotlib.dates as mdates

def make_graph(clusters, title):
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
    plt.title(title)
    plt.legend()

    # グラフを表示
    plt.show()