# coding:utf8
import time
from xml.dom.minidom import Document


doc = Document()  #创建DOM文档对象
# root_node = doc.createElement('vehicleInformation')
# doc.appendChild(root_node)

DOCUMENT = doc.createElement('vehicle') #创建根元素
DOCUMENT.setAttribute('vinLong',"TBD1")#设置命名空间
#DOCUMENT.setAttribute('xsi:noNamespaceSchemaLocation','DOCUMENT.xsd')#引用本地XML Schema
doc.appendChild(DOCUMENT)

############item:Python处理XML之Minidom################
item = doc.createElement('item')
#item.setAttribute('genre','XML')
DOCUMENT.appendChild(item)

key = doc.createElement('key')
key_text = doc.createTextNode('Key1') #元素内容写入
key.appendChild(key_text)
item.appendChild(key)

display = doc.createElement('display')
# item.appendChild(display)
display_url = doc.createElement('url')
display_title  = doc.createElement('title')
display_url_text = doc.createTextNode(time.strftime('%Y%m%d'))
display_title_text  = doc.createTextNode('哈哈')
display.appendChild(display_url)
display.appendChild(display_title)
display_url.appendChild(display_url_text)
display_title.appendChild(display_title_text)
item.appendChild(display)
'''
price = doc.createElement('price')
price_text = doc.createTextNode('28')
price.appendChild(price_text)
item.appendChild(price)
'''
########### 将DOM对象doc写入文件
f = open('test_005.xml','w')
#f.write(doc.toprettyxml(indent = '\t', newl = '\n', encoding = 'utf-8'))
doc.writexml(f,indent = '\t',newl = '\n', addindent = '\t',encoding='utf-8')
f.close()