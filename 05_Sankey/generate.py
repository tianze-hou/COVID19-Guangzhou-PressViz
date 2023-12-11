import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
from pyecharts.charts import Sankey
from pyecharts import options as opts
import os

# 从 input.csv 中读取数据
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.csv')
df = pd.read_csv(filename, header=None)

# 将所有节点去重保存
nodes = []
for i in range(3):
    values = df.iloc[:,i].unique()
    for value in values:
        dic = {}
        dic['name'] = value
        nodes.append(dic)

# 计算每个流动的数量
first = df.groupby([0,1])[3].sum().reset_index()
second = df.iloc[:,1:]
first.columns = ['source','target','value']
second.columns = ['source','target','value']
result = pd.concat([first,second])

# 建立连接
links = []
for i in result.values:
    dic = {}
    dic['source'] = i[0]
    dic['target'] = i[1]
    dic['value']  = i[2]
    links.append(dic)

# 创建Sankey图
pic = (
    Sankey()
    .add('',
         nodes,
         links,
         linestyle_opt=opts.LineStyleOpts(opacity=1, curve=0.5, color='source'),
         label_opts=opts.LabelOpts(position = 'right'),
         node_gap = 25,
        )
)


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'output.html')
pic.render(filename)