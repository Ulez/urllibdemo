# coding:utf-8
import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup

url = "https://passport.csdn.net/account/verify"
cookieJar = cookielib.CookieJar()
processor = urllib2.HTTPCookieProcessor(cookieJar)
opener = urllib2.build_opener(processor)
opener.addheaders = [("User-Agent",
                      "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")]
request = urllib2.Request(url=url)
response = opener.open(request)
dic = {}
lt = BeautifulSoup(response.read(), 'html.parser')
for line in lt.form.findAll('input'):
    try:
        if (line.attrs['name'] != None):
            dic[line.attrs['name']] = line.attrs['value']
            print  line.attrs['name'] + ":" + line.attrs['value']
    except (KeyError), e:
        print 'KeyError'
print dic
formdata = {"gps": "",
            "username": "xx@qq.com",
            "password": "xx",
            "rememberMe": "true",
            "lt": dic['lt'],
            "execution": dic['execution'],
            "fkid": dic['fkid'],
            "_eventId": "submit"}
print formdata
request = urllib2.Request(url=url, data=urllib.urlencode(formdata))
print request.headers
print opener.open(request).read()
