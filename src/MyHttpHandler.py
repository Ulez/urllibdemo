#coding:utf-8
import urllib2

handler = urllib2.HTTPHandler(debuglevel=1)#添加debug，输出发送的信息，header
opener = urllib2.build_opener(handler)
request = urllib2.Request("http://www.baidu.com/")
print opener.open(request).read()
