import Estimated_Time_Spent.clustering as clustering
import Estimated_Time_Spent.graph as graph
import Estimated_Time_Spent.date as date
import pandas as pd
import numpy as np

def main():
    # CSVファイルからデータを読み込む
    file_path = 'processed_data/hayashi_09-12.csv'  # ファイルパスを適切に設定
    df = pd.read_csv(file_path, delimiter=',')  # タブ区切りの場合
    df = date.identification_day(df)

    # 1. 曜日ごとにDataFrameを分割
    # 2. 分割したDataFrameごと文字列をdatetime型に変換
    # 3. 時間データを秒単位に変換
    # 4. クラスタリングの実行
    # 5. 月〜日曜日まで7回繰り返す
    # 6. 結果の出力
    # 7. グラフの作成

    # 曜日ごとのデータを格納するリスト
    # 月曜日: 0, 日曜日: 6
    df_day = []
    # 結果格納用のリスト
    result_entry = []
    result_exit = []

    # 5. 月〜日曜日まで7回繰り返す
    for i in range(7):
        # 1. 曜日ごとにDataFrameを分割
        df_day.append(df[df['day'] == i])
        df_day[i] = df_day[i].reset_index(drop=True)
        # print(f"曜日{i}のデータ")
        print(df_day[i])

        # 2. 分割したDataFrameごと文字列をdatetime型に変換
        df_entry = df_day[i]['entry'].to_list()
        df_exit = df_day[i]['exit'].to_list()
        # print(df_entry)

        # 3. 時間データを秒単位に変換
        data_seconds_entry = np.array([sum(x * float(t) for x, t in zip([3600, 60, 1], point.split(":"))) for point in df_entry])
        data_seconds_exit   = np.array([sum(x * float(t) for x, t in zip([3600, 60, 1], point.split(":"))) for point in df_exit])

        # 4. クラスタリングの実行
        # 結果をリストに格納
        result_entry.append(clustering.xmeans(data_seconds_entry))
        result_exit.append(clustering.xmeans(data_seconds_exit))

    # 6. 結果の出力
    print("入室時刻の結果")
    # print(result_entry)
    for i, result_entry_day in enumerate(result_entry):
        print(f"曜日{i}のデータ")
        for j, cluster in enumerate(result_entry_day):
            centroid_time = cluster["centroid"]
            cluster_points = cluster["points"]
            print(f"Cluster {j + 1}: Centroid = {centroid_time}, Points = {cluster_points}")

    print("")
    print("")

    print("退室時刻の結果")
    # print(result_exit)    
    for i, result_exit_day in enumerate(result_exit):
        print(f"曜日{i}のデータ")
        for j, cluster in enumerate(result_exit_day):
            centroid_time = cluster["centroid"]
            cluster_points = cluster["points"]
            print(f"Cluster {j + 1}: Centroid = {centroid_time}, Points = {cluster_points}")

    # 7. グラフの作成
    graph.make_graph(result_entry, "hayashiの入室時刻")
    graph.make_graph(result_exit, "hayashiの退室時刻")