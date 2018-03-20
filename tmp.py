#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 在这里尝试对爬取下来的数据进行可视化处理
import dataoptions as dp
import matplotlib.pyplot as plt
import datetime

df = dp.DataOptions()
#

# info=df.getJobsInfo('C++')
# print(info)

num = df.getJobInCity()
print(num)
# sorted返回的是一个列表
tmp = sorted(num.items(), key=lambda x: x[1])

plt.figure(figsize=(8, 5), dpi=80)
# ax=plt.subplot(111)

# 用来正常显示中文标签和正负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

time = i = datetime.datetime.now()

plt.title(str(time.year) + '/' + str(time.month) + '/' + str(time.day) + '职位分布图')
plt.bar(num.keys(), num.values(), label="职位数")
plt.legend()    # 显示图例

plt.show()
