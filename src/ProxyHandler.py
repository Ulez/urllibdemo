import urllib2

handler = urllib2.HTTPHandler()
opener = urllib2.build_opener(handler)
request = urllib2.Request("http://www.baidu.com/")
print opener.open(request).read()
