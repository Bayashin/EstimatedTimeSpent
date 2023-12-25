import Estimated_Time_Spent.clustering as clustering
import Estimated_Time_Spent. graph as graph
import pandas as pd
import numpy as np

def main():
    # CSVファイルからデータを読み込む
    file_path = 'processed_data/hayashi_09-10.csv'  # ファイルパスを適切に設定
    df = pd.read_csv(file_path, delimiter=',')  # タブ区切りの場合
    # 時間の文字列をdatetime型に変換
    df_entry = df['entry'].to_list()
    df_exit = df['exit'].to_list()

    # 時間データを秒単位に変換
    data_seconds_first = np.array([sum(x * float(t) for x, t in zip([3600, 60, 1], point.split(":"))) for point in df_entry])
    # data_seconds_end   = np.array([sum(x * float(t) for x, t in zip([3600, 60, 1], point.split(":"))) for point in df_exit])

    # クラスタリングの実行
    result_first = clustering.xmeans(data_seconds_first)
    # result_end = clustering.xmeans(data_seconds_end)

    # 結果の出力
    # print(result_first)
    # for i, cluster in enumerate(result_first):
    #     centroid_time = cluster["centroid"]
    #     cluster_points = cluster["points"]
        
    #     print(f"Cluster {i + 1}: Centroid = {centroid_time}, Points = {cluster_points}")

    # グラフの作成
    graph.make_graph(result_first, "hayashiの入室時刻")
    # graph.make_graph(result_end, "hayashiの退室時刻")