# -*- coding:utf-8 -*-
"""
作者：nuomi
日期：2023年01月18日
"""
import urllib
# 导入pprint，用于以漂亮的方式打印数据结构
from pprint import pprint

import requests

# https://weibo.com/newlogin?tabtype=search&openLoginLayer=0&url=https%3A%2F%2Fwww.weibo.com%2F
# 接口
url = "https://weibo.com/ajax/statuses/hot_band"
# 访问接口
test = requests.get(url)
# 输出访问状态
print(test)
# 获取json数据
json_date = test.json()
# 获取值
test1 = json_date['data']['band_list']
# 字符串拼接用
text = 'https://s.weibo.com/weibo?q=%23'
# 创建列表
list = []
# 循环获取
for i in range(0, 50):
    if i > 50:
        break
    # 转编码
    json_text = urllib.parse.quote(test1[i]['word'])
    # 输出信息
    json_content = i, test1[i]['word'], "热搜值:%s" % test1[i]['num'], "链接:" + text + json_text + '%23'
    # 循环写入列表
    list.append(json_content)

    # print(i, test1[i]['word'], "热搜值:", test1[i]['num'], "链接:", text + json_text + '%23')
else:
    # print(list)
    # 调用pprint来使输出变得漂亮
    pprint(list)

from flask import Flask, jsonify

data = list
app = Flask(__name__)  # 创建一个服务，赋值给APP


@app.route('/get_json', methods=['get'])  # 指定接口访问的路径，支持什么请求方式get，post
# 讲的是封装成一种静态的接口，无任何参数传入
def get_user():  # -----这里的函数名称可以任意取
    return jsonify(data)  # 把字典转成json串返回


app.run(host='0.0.0.0', port=9010, debug=True)
# 这个host：windows就一个网卡，可以不写，而liux有多个网卡，写成0:0:0可以接受任意网卡信息,
# 通过访问127.0.0.1:9669/get_json，可返回data信息
# debug:调试的时候，可以指定debug=true；如果是提供接口给他人使用的时候，debug要去掉
