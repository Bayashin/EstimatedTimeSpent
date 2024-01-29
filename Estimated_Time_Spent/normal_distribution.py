import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import japanize_matplotlib
from sklearn.neighbors import KernelDensity

def convert_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def normal_distribution(data, label, color, n, day_count):
    # print(data)
    # 時刻データを秒に変換
    time_seconds = np.array([convert_to_seconds(t) for t in data])
    # x軸の値を生成
    x_vals = np.linspace(0, 86400, 1000)
    # 確率密度関数を計算
    pdf_vals = norm.pdf(x_vals, loc=np.mean(time_seconds), scale=np.std(time_seconds))* n/day_count
    plt.plot(x_vals, pdf_vals, color=color, label=label)

def density_estimation_graph(data):
    # print(data)
    # データセットごとに確率密度関数をプロット
    if len(data) == 1:
        normal_distribution(data[0], 'Dataset 1', 'red')
    else:
        colors = ['red', 'blue', 'green']
        for i, data_set in enumerate(data):
            normal_distribution(data_set, f'Dataset {i+1}', colors[i])
    # グラフの設定
    plt.xlabel('Time (seconds)')
    plt.ylabel('Probability Density')
    plt.title('Probability Density Functions')
    plt.legend()
    plt.show()

# timeが発生する確率を計算
def probability_from_normal_distribution(data, time, day_count):
    l=0
    probabilities = []
    for i, datum in enumerate(data):
        # 時刻データを秒に変換
        data_seconds = np.array([convert_to_seconds(t) for t in datum])
        # print("data_seconds")
        # print(data_seconds)
        time_seconds = np.array(convert_to_seconds(time))
        # for _, data_second in enumerate(data_seconds):
        # print("data_second")
        # print(data_seconds)
        # print(len(data_seconds))
        if len(data_seconds) == 1:
            continue
        loc = np.mean(data_seconds)
        scale = np.std(data_seconds)
        probabilities.append(norm.cdf(time_seconds, loc, scale)* len(data_seconds)/day_count)
        print(f"{l+1}番目の確率: {probabilities[l]*100:.2f}%")
        l += 1
    # timeより前に研究室に来ている割合を計算
    probability = np.sum(probabilities)
    print(f"{time}までに研究室に来ている確率は{probability*100:.2f}%です。")
    print(f"{convert_to_seconds(time)}までに研究室に来ている確率は{probability*100:.2f}%です。")