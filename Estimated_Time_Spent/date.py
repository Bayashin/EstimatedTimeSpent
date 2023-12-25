import pandas as pd
from datetime import datetime

def identification_day(df = pd.DataFrame()):
    # 日付から曜日を取得してDataFrameに追加
    # CSVファイルからデータを読み込む
    # file_path = 'processed_data/hayashi_09-10.csv'  # ファイルパスを適切に設定
    # df = pd.read_csv(file_path, delimiter=',')  # タブ区切りの場合
    # 時間の文字列をdatetime型に変換
    df_date= df['date'].to_list()

    day = []
    for i in range(len(df_date)):
        date_object = datetime.strptime(df_date[i], '%Y-%m-%d')
        day.append(date_object.weekday())

    df['day'] = day
    # print(df)
    return df

