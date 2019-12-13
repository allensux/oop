# coding:utf8
import requests
from bs4 import BeautifulSoup

# newsurl = "http://news.baidu.com/"
newsurl = "http://news.baidu.com/guonei"
res = requests.get(newsurl) # 取得页面所有内容
# print(res.encoding) # 网页编码格式
result = res.text
# print("网页内容：",result) # 获取网页内容

soup = BeautifulSoup(result, 'html.parser')
# header = soup.select('.bold-item')  # 取全部class为bold-item的元素
# #header = soup.select('#news-hotwords')  # 使用select找到所有id为news-hotwords的元素
# header = soup.select('a')  # 使用select找到所有a tag的href链接

header = soup.select('.ulist')  # 取全部class为ulist 的元素
print("header内容为:",header)
for news in header:
    print(news.select('li')[0].text)
    print(news.select('a')[1]['href'])
    # print(news)
# for link in header:
#
#     # print(link)
#     alink = link['href']
#     print(alink)
# print(header)
# for link in header:
#     print(link.text)
