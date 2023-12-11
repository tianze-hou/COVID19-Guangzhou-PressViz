import numpy as np
import matplotlib.pyplot as plt
import squarify as sq
import os

# 输入数据、定义颜色
volume = [143,36,22]
color_list = ['#009BF1', '#1F52A0', '#78CFF1']

# 绘制矩形
sq.plot(sizes=volume, color=color_list)
plt.axis('off')

# 将图表保存为 SVG 矢量图并导出
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'output.svg')
plt.savefig(filename)

# 显示图表
plt.show()