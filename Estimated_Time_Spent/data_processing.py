import pandas as pd
from datetime import datetime

# CSVファイルからデータを読み込む
file_path = 'raw_data/kaji_09-10.csv'  # ファイルパスを適切に設定
df = pd.read_csv(file_path, delimiter=',')  # タブ区切りの場合

# 時間の文字列をdatetime型に変換
df['start_at'] = pd.to_datetime(df['start_at'])
df['end_at'] = pd.to_datetime(df['end_at'])

# 日付ごとに最初の入室と最後の入室を取得
result_data = []
grouped_data = df.groupby(df['start_at'].dt.date)
for date, group in grouped_data:
    first_entry = group.loc[group['start_at'].idxmin()]
    last_exit = group.loc[group['start_at'].idxmax()]
    
    result_data.append({
        'Date': date,
        'First Entry': first_entry['start_at'].strftime('%H:%M:%S.%f')[:-3],
        'Last Exit': last_exit['end_at'].strftime('%H:%M:%S.%f')[:-3]
    })

# 結果をDataFrameに変換してCSVに書き込む
result_df = pd.DataFrame(result_data)
result_df.to_csv('processed_data/kaji_09-10.csv', index=False)
