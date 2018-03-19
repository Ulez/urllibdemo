import urllib2
import urllib


def writePage(html, filename):
    print("saving page...")
    with open(filename, "w") as f:
        f.write(html)


def getPage(url):
    print("loading page..." + url)
    uheaders = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    }
    request = urllib2.Request(url, headers=uheaders)
    response = urllib2.urlopen(request)
    return response.read()


def tiebaSpider(url, startPage, endPage):
    for page in range(startPage, endPage + 1):
        pn = (page - 1) * 50
        fullurl = url + "&pn=" + str(pn)
        writePage(getPage(fullurl), "index-" + str(page) + ".html")


if __name__ == "__main__":
    # https://tieba.baidu.com/f?kw=dota2&fr=index
    kw = raw_input("input tieba name")
    startPage = int(raw_input("input start page"))
    endPage = int(raw_input("input end page"))
    url = "https://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, startPage, endPage)
