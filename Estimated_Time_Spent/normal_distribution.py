import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import japanize_matplotlib
from sklearn.neighbors import KernelDensity

def convert_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def normal_distribution(data, label, color):
    print(data)
    # 時刻データを秒に変換
    time_seconds = np.array([convert_to_seconds(t) for t in data])

    # x軸の値を生成
    x_vals = np.linspace(0, 86400, 1000)

    # 確率密度関数を計算
    pdf_vals = norm.pdf(x_vals, loc=np.mean(time_seconds), scale=np.std(time_seconds))
    plt.plot(x_vals, pdf_vals, color=color, label=label)

def density_estimation_graph(data):
    print(data)
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