import os
import pandas as pd
import matplotlib.pyplot as plt

# 读取csv文件
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.csv')
df = pd.read_csv(filename, header=None)

# 转化为列表
tasks = []
for i, row in df.iterrows():
    start_date = row[0]
    end_date = row[1]
    name = row[2]
    color = row[3]
    tasks.append((start_date, end_date, name, color))

# 创建坐标轴
fig, ax = plt.subplots()

# 建立颜色表，用颜色深度表示一天内多场发布会
colors = ['#EBF5FB', '#D6EAF8', '#AED6F1', '#85C1E9', '#5DADE2', '#3498DB']

# 遍历列表，转换为传递给broken_brah的参数
for start, end, name, color in tasks:
    start_date = pd.to_datetime(start)
    end_date = pd.to_datetime(end)
    duration = end_date - start_date
    if name == '共564场（模拟）': yname = (8, 0.8)
    if name == '所有信源': yname = (7, 0.8)
    if name == '广州市新闻中心': yname = (6, 0.8)
    if name == '广州市卫健委': yname = (5, 0.8)
    if name == '中国广州发布': yname = (4, 0.8)
    if name == '广州市政府网站': yname = (3, 0.8)
    if name == '中国网广州发布': yname = (2, 0.8)
    if name == '广州市司法局': yname = (1, 0.8)
    if name == '广州各区发布公众号': yname = (0, 0.8)

    # 绘制矩形色块
    ax.broken_barh([(start_date, duration)], yname, facecolors=colors[int(color-1)])

# 设置坐标轴字体和可见性
plt.xticks(size = 5)
plt.yticks([])
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)

# 将图表保存为 SVG 矢量图并导出
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'output.svg')
plt.savefig(filename)

# 显示图表
plt.show()