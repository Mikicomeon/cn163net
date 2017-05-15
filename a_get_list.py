#-*- coding:utf-8 -*-
import requests
from lxml import etree
from bs4 import BeautifulSoup
from public.mysqlpooldao import MysqlDao
import traceback

mysql_dao = MysqlDao()

if __name__ == '__main__':
    url = 'http://cn163.net/ddc1/ddc3/'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'cn163.net',
        'Referer' : 'http://cn163.net/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    res = requests.get(url)
    wb_data = res.content
    selector = etree.HTML(wb_data)
    proxy_lists = selector.xpath('//ul[@class="sub-menu"]/li')
    print len(proxy_lists)

    for proxy_list in proxy_lists[:6]:
        url = proxy_list.xpath('a/@href')
        category_name = proxy_list.xpath('a/text()')
        if len(url) > 0:
            url = url[0]
        if len(category_name) > 0 :
            category_name = category_name[0]
        print url,category_name
        sql = 'INSERT ignore INTO `meiju_category_list` (`category_name`,`url`) VALUES("%s","%s")' % (category_name,url)
        print sql
        try:
            mysql_dao.execute(sql)
        except Exception as e:
            traceback.print_exc()
            print sql
            print e



# def get_BBC_video():
#     sql = 'INSERT ignore INTO `meiju_category_list` (`category_name`,`url`) VALUES("%s","%s")' % ('BBC纪录片', 'http://cn163.net/bbcjilu/')
#     print sql
#     try:
#         mysql_dao.execute(sql)
#     except Exception as e:
#         traceback.print_exc()
#         print sql
#         print e
#
# get_BBC_video()