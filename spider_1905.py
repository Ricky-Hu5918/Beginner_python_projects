#import libs
import requests
import re

import sys
# reload(sys)
# sys.setdefautencoding('utf8')

# 确认访问地址
url = 'https://www.1905.com/mtalk/'

# 确定查找规则，正则表达式, (.*?)表示获取所有内容
pattern = '<figcaption class="list-title"><a href="(.*?)" target="_blank">(.*?)</a></figcaption>'

# 加一个请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}

# 请求地址
response = requests.get(url=url, headers=header)

# 返回200，说明连接成功
# print(response)

# 注意编码按照页面的编码来制定
response.encoding = 'utf8'

# 打印输出网页内容，跟浏览器右键检查查看效果一样
# print(response.text)

# 查找匹配想要爬取的信息， flags=re.S是防止所要爬取的信息过长，从而换行，导致爬取信息不全
result = re.findall(string=response.text, pattern=pattern, flags=re.S)
# print(result)  # 返回的结果是元组形式
# for i in result:
#     for j in i:
#         print(j)

# for i in result:
#     print(i[1], i[0] + '\n')

# 将爬取到的信息写入文件
j = 0
for i in result:
    j += 1
    with open('2021-2.txt', 'a') as w:
        w.write(str(j) + '.' + i[1]+'  '+i[0]+'\n')
