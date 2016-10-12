#coding=utf-8
import hashlib
import requests
import json
import traceback
import urllib2
from scrapy.http import HtmlResponse
import StringIO
hdrs = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

#img_url = 'http://r.weizhang8.cn/mysource/validatecode/code_gg.php'
#r = requests.get(img_url,headers = hdrs)
#print r.headers['content-type']
#aaa = StringIO.StringIO(r.content)
#print aaa



# import urllib2
# import cookielib
#
# # c = cookielib.CookieJar()
# # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(c))
# # login_path = "http://gsxt.gdgs.gov.cn/aiccips/"
# #
# #
# # request = urllib2.Request(login_path, headers = hdrs)
# # html = opener.open(request).read()
# # print c
#
# import requests
# session=requests.session()
#
# proxies = {"http": "119.6.136.122:80"}
#
#
# # url='http://www.tianyancha.com/search/%E7%99%BE%E5%BA%A6?checkFrom=searchBox'
# # headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
# aaa=session.get(url='http://gsxt.gdgs.gov.cn/aiccips/',headers=hdrs, proxies = proxies)
# cookies_dict=aaa.cookies.get_dict()
# print aaa.cookies
# print cookies_dict
# print aaa.headers['set-cookie']

# url = 'http://tjcredit.gov.cn/platform/saic/viewBase.ftl?entId=006fa20e53ee8a1e0e8075326fa3f020'
# body = '<td class="bg" width="22%">Ӫҵִ��ע���</br>ͳһ������ô���</td> <td class="" width="30%">aaaaaaaaaa<br/>bbbbbbbbbbb</td>'
#
# response = HtmlResponse(url = url, body = body)
# print response.xpath('//td/text()').extract()
# print len(response.xpath('//td/text()').extract())

def test():
    while (1):
        return "11111111111"

print test()