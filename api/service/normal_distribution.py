from __future__ import annotations
from scipy.stats import norm
from ..models import struct as st

def convert_to_seconds(time_str :str) -> int:
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

# timeが発生する確率を計算
def probability_from_normal_distribution(clusters: list[st.Cluster], time: str, day_count: int, yn: bool) -> float:
    probabilities: list[float] = []
    for cluster in clusters:
        # 時刻データを秒に変換
        time_seconds = convert_to_seconds(time)
        if yn:
            # timeより前に研究室に来ている割合を計算
            probabilities.append(norm.cdf(time_seconds, cluster.average, cluster.sd)* cluster.count/day_count)
        else:
            # timeより後に研究室に来ている割合を計算
            probabilities.append((1 - norm.cdf(time_seconds, cluster.average, cluster.sd))* cluster.count/day_count)
    probability = sum(probabilities)
    return probability
    # if yn:
    #     print(f"{time}までに研究室に来ている確率は{probability*100:.2f}%です。")
    # else:
    #     print(f"{time}以降に研究室に来ている確率は{probability*100:.2f}%です。")