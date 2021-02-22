from os import link
from sqlite3.dbapi2 import connect
import requests
import sqlite3
import json
import random

# 建立一个函数find()


def find():
    # 确认访问地址
    # Request URL: https://www.1905.com/api/content/?callback=reloadList&m=converged&a=info&type=jryp&year=2021&month=1
    # 从Request URL分析，访问地址分为两部分，问号之前的为固定的地址，问好之后的为参数，即params
    url2 = 'https://www.1905.com/api/content/'

    # 加一个请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    # 确定请求参数
    params = {
        'callback': 'reloadList',
        'm': 'converged',
        'a': 'info',
        'type': 'jryp',
        'year': '2021',
        'month': '2',
    }

    # 请求地址
    response = requests.get(url=url2, headers=header, params=params)

    # 注意编码按照页面的编码来制定
    #response.encoding = 'utf8'

    # 返回200，说明连接成功
    # print(response)

    # 打印输出网页内容，跟浏览器右键检查查看效果一样
    result = response.text
    # print(result)

    #去掉头部的reloadList( 和尾部的 ), 把字符串剥离成元组的形式
    result = result.replace('reloadList(', '').replace(')', '')
    # print(result)

    #把json字符串转成字典格式用json.loads(), 反过来把字典格式转成json字符串用json.dumps()
    result = json.loads(result)

    # 读取需要的数据，此处是从info中读取
    # 此处爬取三个数据，名称，链接和图片
    for i in result['info']:
        #print(i['url'], i['title'], i['thumb'])

        # 读取照片，使用content返回一个二进制数据
        img = requests.get(i['thumb']).content

        # 保存图片，用wb，writebytes二进制
        img_name = random.randint(10000, 99999)  # 产生一个随机数作为文件的名字，避免重复
        # with open('img/%s.jpg' % img_name, 'wb') as w:
        #     w.write(img)

        # 调用save_data()方法存储数据
        save_data(content=i['title'], link=i['url'], img=img_name)
        # break


def createdb():  # 创建数据库
    conn = sqlite3.connect('1905.db')
    c = conn.cursor()
    c.execute(
        'CREATE TABLE filmdata (id INTEGER PRIMARY KEY AUTOINCREMENT, content text, link text, img text)')
    conn.commit()
    conn.close()


def save_data(content, link, img):  # 保存爬取的数据
    conn = sqlite3.connect('1905.db')
    c = conn.cursor()
    c.execute("INSERT into filmdata(content, link, img) VALUES ('{0}', '{1}', '{2}')".format(
        content, link, img))
    conn.commit()
    conn.close()


def show_data():  # 查看数据内容
    conn = sqlite3.connect('1905.db')
    c = conn.cursor()
    res = c.execute('SELECT * from filmdata')
    print(res)
    for i in res:
        print(i)
    conn.close()


if __name__ == '__main__':
    # createdb()  #必须先create数据库
    # show_data()
    find()
