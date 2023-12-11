# 数据及代码

## 内容及工作流程说明
本项目为数据可视化作业《三年鏖战，广州疫情新闻发布会跨越终点》的源代码展示。考虑到matplotlib默认配置下对中文支持不佳，以及后期编辑排版中的效率，代码生成的多数图像不包括文字标签，也没有从美观角度考虑进行比较复杂的配置。后期编辑排版使用Adobe Illustrator完成。  

部分数据使用pandas进行了预处理。考虑到csv格式预处理流程方法较多，代码比较简单，此处不再一一展示。  

对于词频统计部分，考虑到StanfordNLP对新词的分词准确率不佳，最终使用了微词云进行分词统计。

## 依赖
Pillow>=8.1.1  
Scrapy>=2.7.1  
requests>=2.28.1  
pandas>=1.5.2  
numpy>=1.24.1  
matplotlib>=3.6.2  
seaborn>=0.12.2  
squarify>=0.4.3  
circlify>=0.15.0  
pyecharts>=2.0.1  

```
$ pip install -r requirements.txt
```

## 数据及代码目录

### 00_raw_data
包含本项目使用的原始数据，包含两个文件：
1. source_text.csv：爬虫结合人工整理的发布会数据。
2. source_wb.csv：爬虫获取的#广州疫情#微博话题内容数据。
3. source_encoding1.csv, source_encoding2.csv：由王睿同学、杨笑薇同学人工编码完成的媒体编码表。

### 01_Type_tree
即“广州疫情新闻发布会构成”图表的源代码，由侯天泽同学编写并完成后期编辑。 源数据由王睿、杨笑薇同学人工编码完成。   
使用sqyarify库生成矩形树图并绘制为output.svg，后期使用Adobe Illustrator进行编辑和排版。
output.svg为程序运行导出的结果。后期使用Adobe Illustrator进行编辑和排版。

### 02_Source_chart
即“广州疫情新闻发布会正文公开来源”图表的源代码，由侯天泽同学编写并完成后期编辑。  
事先使用pandas将原始数据source_text.csv处理为input.csv，作为用于本表的数据。  
使用pandas读取input.csv数据，使用matplotlib的ax.broken_barh函数绘制矩形色块。  
output.svg为程序运行导出的结果。后期使用Adobe Illustrator进行编辑和排版。

### 03_Frequency_histograph
即“广州疫情新闻发布会召开频率”图表的源代码，由侯天泽同学编写并完成后期编辑。  
事先使用pandas将原始数据source_text.csv处理为input.csv，作为用于本表的数据。  
使用pandas将数据分组，使用matplotlib的subplots函数创建子图，使用figure和axes对象设置子图布局和样式，使用matplotlib的bar函数在每个子图上绘制柱状图。  
output.svg为程序运行导出的结果。后期使用Adobe Illustrator进行编辑和排版。

## 04_Spokesperson_circle_packing
即“出席发言人所属单位类型”图表的源代码，由侯天泽同学编写并完成后期编辑。源数据由王睿同学制定编码表，并由侯天泽同学完成频率统计，形成input.csv文件。  
使用pandas读取input.csv，通过遍历所有行，计算同一类型媒体被提及的总次数存储在字典中，将键和值导出保存到csv，将值转换为sizes列表，使用circlify包的功能计算圆圈位置，确保圆圈在画布内并绘图生成svg。  
该代码生成的svg图片比较简单，主要用于创建大小符合数据情况的圆形，结合输出csv文件进行编辑。后期使用Adobe Illustrator进行编辑和排版。

## 05_weibo_crawl
使用开源项目“[weibo-search](https://github.com/dataabc/weibo-search)”的代码，分多次爬取2020-01-28至2022-12-07之间微博话题#广州疫情#下的微博。程序由侯天泽同学调试运行，并手动剔除了其中的机构媒体账号、营销号、转载官方发布内容及无关内容。本文件夹中展示的wb_data.csv是经剔除后的版本，原始数据详见/00_raw_data/source_wb.csv。分词统计及排版编辑使用微词云和Adobe Illustrator完成。  
考虑到个人隐私，我们在weibo-search的配置文件中删除了爬虫中使用的cookies，导致该程序当前**无法运行**。如需检查该代码，请在/06_weibo_crawl/weibo/settings.py中的相应位置增加可用的微博账号cookies。

## 06_Sankey
此处展示了“广州疫情新闻发布会提问媒体概览”可交互版本的代码。源数据由王睿同学和杨笑薇同学手动编码，由侯天泽同学使用pandas预处理为inpus.csv，并编写Sankey图代码。该代码使用pyecharts包的Sankey函数创建Sankey图。  
考虑到matplotlib中文兼容性不佳，而pyecharts并没有类似matplotlib中tight_layout函数功能来减少重叠提高可读性，pdf中最终呈现的不可交互版本由侯天泽同学使用开源项目[rawgraphs-app](https://github.com/rawgraphs/rawgraphs-app)制作。

## 其他图表制作情况
- “广州疫情新闻发布会词云”由侯天泽同学使用微词云分词工具和Adobe Illustrator编辑制作。
- “广州各区三年受疫情波及程度”由侯天泽同学使用matplotlib的get_cmap函数生成颜色，之后使用Adobe Illustrator编辑制作。
- “发布会中发言人来自哪些单位”由王睿同学基于编码数据使用Adobe Photoshop制作完成。
- “广州疫情新闻发布会媒体提问变化”由杨笑薇同学使用[Flourish](https://app.flourish.studio/templates)工具制作。
- “发布会中疫情相关高频词汇变化”由侯天泽同学使用开源项目[rawgraphs-app](https://github.com/rawgraphs/rawgraphs-app)制作。
- “广州疫情新闻发布会三年内容主题频次”由杨笑薇同学使用[Flourish](https://app.flourish.studio/templates)工具制作。
