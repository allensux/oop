# coding:utf8

managerList = [{'name' : 'joy', 'age' : 27, 'sex' : '女'},{'name' : 'tom', 'age' : 30, 'sex' : '男'},{'name' : 'ruby', 'age' : 29, 'sex' : '女'} ]
from xml.dom import minidom
doc=minidom.Document()


managers=doc.createElement('Managers')
managers.setAttribute('address',u'科技软件园')
managers.setAttribute('company',u'xx科技')
doc.appendChild(managers)
for i in range(3):
    manager=doc.createElement('manager')
    name=doc.createElement(managerList[i].keys())
    name.appendChild(doc.createTextNode(str(managerList[i].values())))
    age=doc.createElement(managerList[i].keys())
    age.appendChild(doc.createTextNode(managerList[i].values()))
    sex=doc.createElement(managerList[i].keys())
    sex.appendChild(doc.createTextNode((managerList[i].values()).decode('utf-8')))
    manager.appendChild(name)
    manager.appendChild(age)
    manager.appendChild(sex)
    managers.appendChild(manager)


import codecs
f=codecs.open(r'C:\Users\libai\Desktop\xml1\text3.xml','w','utf-8')
doc.writexml(f,indent=' ',addindent='   ',newl='\n',encoding='utf-8')
f.close()