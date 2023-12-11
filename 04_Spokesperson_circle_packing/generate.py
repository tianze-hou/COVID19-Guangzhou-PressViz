import pandas as pd
import matplotlib.pyplot as plt
import circlify
import os
import csv

# 从 input.csv 中读取数据
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.csv')
df = pd.read_csv(filename, header=None)

# 计算同一类型媒体被提及的总次数
sums = {}
for index, row in df.iterrows():
    name = row[0]
    value = row[2]
    if name in sums:
        sums[name] += value
    else:
        sums[name] = value

# 将字典写csv，并转换为后续可用的列表
with open(os.path.join(dirname, 'output.csv'),'w') as f:
    writer = csv.writer(f)
    for key, value in sums.items():
        writer.writerow([key, value])
sizes = list(sums.values())

# 计算圆圈位置
circles = circlify.circlify(sizes, show_enclosure=False, target_enclosure=circlify.Circle(x = 0, y = 0, r = 1))

# 创建画布
fig, ax = plt.subplots(figsize=(10,10))

# 关闭坐标轴
ax.axis('off')

# 确保圆圈在画布范围内
lim = max(max(abs(circle.x) + circle.r, abs(circle.y) + circle.r,)
    for circle in circles)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)


# 创建圆圈
for circle in circles:
    print(circle)
    x, y, r = circle
    ax.add_patch(plt.Circle((x,y),r, linewidth = 2, fill = False))

# 将图表保存为 SVG 矢量图并导出
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'output.svg')
plt.savefig(filename)

# 显示图表
plt.show()