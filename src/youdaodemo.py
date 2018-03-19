import urllib
import urllib2

word = raw_input("input a word to translate:")
uheaders = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Host": "fanyi.youdao.com",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
formdata = {"i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": "1521469191980",
            "sign": "dc1a71c8e599af120984dc399917c9ee",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTIME",
            "typoResult": "false"}

request = urllib2.Request(url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule",
                          data=urllib.urlencode(formdata),
                          headers=uheaders)

print urllib2.urlopen(request).read()
