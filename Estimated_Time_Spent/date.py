import pandas as pd
from datetime import datetime

def identification_day(df = pd.DataFrame()):
    
    # 時間の文字列をdatetime型に変換
    df_date= df['date'].to_list()

    # 日付から曜日を取得してDataFrameに追加
    day = []
    for i in range(len(df_date)):
        date_object = datetime.strptime(df_date[i], '%Y-%m-%d')
        day.append(date_object.weekday())

    df['day'] = day
    # print(df)
    return df

def convert_seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"