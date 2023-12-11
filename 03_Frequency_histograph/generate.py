import matplotlib.pyplot as plt
import pandas as pd
import os

# 从 input.csv 中读取数据
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.csv')
df = pd.read_csv(filename, header=None)


# 根据第三列的数字将数据分为六组
group1 = df[df[2] == 1]
group2 = df[df[2] == 2]
group3 = df[df[2] == 3]
group4 = df[df[2] == 4]
group5 = df[df[2] == 5]
group6 = df[df[2] == 6]

# 创建 Figure 和 Axes 对象
fig, axs = plt.subplots(3, 2, figsize=(6, 6))

# 绘制第一组柱状图
axs[0, 0].bar(group1[0], group1[1])
axs[0, 0].set_xlim([0, max(group1[0])])
axs[0, 0].set_ylim([0, 8])

# 绘制第二组柱状图
axs[0, 1].bar(group2[0], group2[1])
axs[0, 1].set_xlim([27, max(group2[0])])
axs[0, 1].set_ylim([0, 8])

# 绘制第三组柱状图
axs[1, 0].bar(group3[0], group3[1])
axs[1, 0].set_xlim([0, max(group3[0])])
axs[1, 0].set_ylim([0, 8])

# 绘制第四组柱状图
axs[1, 1].bar(group4[0], group4[1])
axs[1, 1].set_xlim([27, max(group4[0])])
axs[1, 1].set_ylim([0, 8])

# 绘制第五组柱状图
axs[2, 0].bar(group5[0], group5[1])
axs[2, 0].set_xlim([0, max(group5[0])])
axs[2, 0].set_ylim([0, 8])

# 绘制第六组柱状图
axs[2, 1].bar(group6[0], group6[1])
axs[2, 1].set_xlim([27, max(group6[0])])
axs[2, 1].set_ylim([0, 8])

# 将图表保存为 SVG 矢量图并导出
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'output.svg')
plt.savefig(filename)

# 显示图表
plt.show()