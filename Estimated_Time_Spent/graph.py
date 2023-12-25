import matplotlib.pyplot as plt
import japanize_matplotlib
import matplotlib.dates as mdates
from datetime import datetime

def make_graph(clusters, title):
    day_list = ['月', '火', '水', '木', '金', '土', '日']

    _, axes = plt.subplots(2, 4, figsize=(16, 8))

    for i, cluster_list in enumerate(clusters):
        row, col = divmod(i, 4)
        ax = axes[row, col]

        for j, cluster in enumerate(cluster_list):
            # クラスタのデータを日時オブジェクトに変換（ミリ秒を含む）
            cluster_data = {cluster['centroid']: [datetime.strptime(time, "%H:%M:%S.%f") if '.' in time else datetime.strptime(time, "%H:%M:%S") for time in cluster['points']]}

            for cluster_centroid, times in cluster_data.items():
                ax.scatter(times, [1] * len(times), label=f"Cluster {j + 1}")

            # クラスタのセントロイドをプロット
            centroid_time = datetime.strptime(cluster['centroid'], "%H:%M:%S")
            ax.scatter(centroid_time, 1, c='black', marker='x', s=100, label=f"Centroid {j + 1}")

        # グラフの設定
        ax.yaxis.set_visible(False)  # y軸を非表示にする
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=6))  # x軸のメモリを6時間ごとに表示
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # x軸のフォーマットを設定
        ax.set_xlabel('時間')
        ax.set_title(f"{day_list[i]}曜日の{title}")
        ax.legend()

        # x軸の最小値と最大値を設定
        ax.set_xlim([datetime.strptime('00:00:00', '%H:%M:%S'), datetime.strptime('23:59:59', '%H:%M:%S')])

    plt.suptitle(title, y=1.02)  # グラフ全体のタイトル
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # グラフが重ならないように調整
    plt.show()