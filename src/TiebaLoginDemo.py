#coding:utf-8
import urllib
import urllib2

uheaders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Cookie": "BAIDUID=A02A1CA41381F3D693515E0A79ABF426:FG=1; BIDUPSID=A02A1CA41381F3D693515E0A79ABF426; PSTM=1519880431; TIEBA_USERTYPE=29fdeceb6093c2ae5328b71f; TIEBAUID=a42b78ec9956d8048e02f266; rpln_guide=1; bdshare_firstime=1521902241241; H_PS_PSSID=1463_21093_17001_22159; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=2; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1521902476,1521902685,1522070444,1522070458; baidu_broswer_setup_第三方ds发给=0; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1522070473; FP_UID=002df7cf1fd7bb04a3fb508bfc4139c1; BDUSS=5WU01KdUtBOHl5NHZ4THA5dG52T3hmanpVeTdjVENMRTlBajNzWUtuTGNnT0JhQVFBQUFBJCQAAAAAAAAAAAEAAADtb24gtdrI~be9ZHO3orj4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANzzuFrc87haOW"
}
request = urllib2.Request(
    "http://tieba.baidu.com/home/main?id=ed6fe7acace4b889e696b96473e58f91e7bb996e20&fr=userbar&red_tag=g1669895808",
    headers=uheaders)
response = urllib2.urlopen(request)
print response.read()