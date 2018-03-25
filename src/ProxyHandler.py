# coding:utf-8
import urllib2

# 构建代理；
handler = urllib2.ProxyHandler({"http": "114.113.126.87"})
nullhandler = urllib2.ProxyHandler({})
opener = urllib2.build_opener(handler)
request = urllib2.Request("http://www.baidu.com")
# urllib2.install_opener(opener) #设置一个全局的代理
# urllib2.urlopen(request)
print opener.open(request).read()
