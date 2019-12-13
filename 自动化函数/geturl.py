# coding:utf8

def getUrl(url):
    urls = url.split('/')
    url = urls[0]+'/'+ urls[1] +'/'+ urls[2] + '/' + urls[3] + '/'
    print('url:',url)
    return url
print(getUrl('http://10.10.171.248:7001/rtm/a?sysYear=2019'))
