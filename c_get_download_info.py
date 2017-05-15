#-*- coding:utf-8 -*-
import sys
import requests
from lxml import etree
from public.mysqlpooldao import MysqlDao
from public.headers import Headers
from public.redispooldao import RedisDao
import re
import simplejson
reload(sys)
sys.setdefaultencoding('utf-8')

mysql_dao = MysqlDao()

def get_download_info(subject,url,category_name):
    # url = 'http://cn163.net/archives/2876/'
    # url = 'http://cn163.net/archives/23749/'
    headers = Headers.get_headers()
    res = requests.get(url, headers=headers)
    wb_data = res.content
    selector = etree.HTML(wb_data)

    lines = selector.xpath('//div[@class="entry"]/div[@id="entry"]/p')
    # print len(lines)
    if len(lines)>1:
        line1 = lines[1]
        xx1 = etree.tostring(line1)
        xx = xx1.split('<strong>')
        if len(xx)%2 != 0:
            print u'奇数'
            for t in range(1,len(xx)):   #每一个strong
                xx_xx = '<strong>' + xx[t]     #<strong></strong>  每一季所有集数级内容
                # print xx_xx
                selector1= etree.HTML(xx_xx)
                # print selector1                 #<strong></strong>  每一季所有集数级内容
                content = download_url = download_name =''
                contents = selector1.xpath('//strong/text()')
                if len(contents)>0:
                    # print 'yes'
                    content = contents[0]     #strong里写的第几季
                    # print content
                    downloads =  selector1.xpath('//a')    #所有有链接的集数及url
                    for download in downloads:
                        download_urls = download.xpath('@href')
                        if download_urls:
                            download_url =download_urls[0]
                        download_names = download.xpath('text()')
                        if download_names:
                            download_name =download_names[0]
                        # print download_url,download_name,content
                        values = (subject,url,category_name,download_url,download_name,content)
                        sql1 = 'INSERT INTO cn163_download_info (subject,url,category_name,download_url,download_name,content) VALUES ("%s","%s","%s","%s","%s","%s")'%  values
                        mysql_dao.execute(sql1)
                        print sql1

                    xx_xx_xx = selector1.xpath('//text()')
                    xx_aa = selector1.xpath('//a/text()')
                    output = set(xx_xx_xx) - set(xx_aa)
                    for x in output:
                        abs = re.findall('(.*mp4|.*mkv|.*720P)', x)
                        abs_url = ''
                        if abs:
                            for abs_single in abs:
                                abs_single_text =  abs_single.replace('｜','').replace(u'（','')
                                # print abs_url,abs_single_text,content
                                values = (subject, url, category_name, abs_url,abs_single_text,content)
                                sql2 = 'INSERT INTO cn163_download_info (subject,url,category_name,download_url,download_name,content) VALUES ("%s","%s","%s","%s","%s","%s")' % values
                                mysql_dao.execute(sql2)
                                print sql2






        if len(xx)%2 == 0:
            print u'偶数'
            for t in range(1,len(xx)):
                xx_xx = '<strong>' + xx[t]
                selector1= etree.HTML(xx_xx)
                # print selector1
                contents = selector1.xpath('//strong/text()')
                if len(contents)>0:
                    content = contents[0]
                    # print content
                downloads =  selector1.xpath('//a')
                for download in downloads:
                    download_urls = download.xpath('@href')
                    if download_urls:
                        download_url =download_urls[0]
                    download_names = download.xpath('text()')
                    if download_names:
                        download_name =download_names[0]
                    # print download_url,download_name,content
                    values = (subject, url, category_name, download_url, download_name, content)
                    sql3 = 'INSERT INTO cn163_download_info (subject,url,category_name,download_url,download_name,content) VALUES ("%s","%s","%s","%s","%s","%s")' % values
                    mysql_dao.execute(sql3)
                    print sql3

                xx_xx_xx = selector1.xpath('//text()')
                xx_aa = selector1.xpath('//a/text()')
                output = set(xx_xx_xx) - set(xx_aa)
                for x in output:
                    abs = re.findall('(.*mp4|.*mkv|.*720P)', x)
                    abs_url = ''
                    if abs:
                        for abs_single in abs:
                            abs_single_text =  abs_single.replace('｜', '').replace(u'（', ''), abs_url, content
                            # print abs_url, abs_single_text, content
                            values = (subject, url, category_name, abs_url, abs_single_text, content)
                            sql4 = 'INSERT INTO cn163_download_info (subject,url,category_name,download_url,download_name,content) VALUES ("%s","%s","%s","%s","%s","%s")' % values
                            mysql_dao.execute(sql4)
                            print sql4

    if len(lines) == 1:
        line2 = lines[0]
        xx1 = etree.tostring(line2)
        xx = xx1.split('<strong>')
        # print len(xx)
        if len(xx) % 2 != 0:
            print u'奇数'
            for t in range(1, len(xx)):
                xx_xx = '<strong>' + xx[t]
                selector1 = etree.HTML(xx_xx)
                # print selector1
                content = download_url = download_name = ''
                contents = selector1.xpath('//strong/text()')
                if len(contents) > 0:
                    content = contents[0]
                    # print content
                    downloads = selector1.xpath('//a')
                    for download in downloads:

                        download_urls = download.xpath('@href')
                        if download_urls:
                            download_url = download_urls[0]
                        download_names = download.xpath('text()')
                        if download_names:
                            download_name = download_names[0]
                        # print download_url, download_name,content
                        values = (subject, url, category_name, download_url, download_name, content)
                        sql5 = 'INSERT INTO cn163_download_info (subject,url,category_name,download_url,download_name,content) VALUES ("%s","%s","%s","%s","%s","%s")' % values
                        mysql_dao.execute(sql5)
                        print sql5

                    xx_xx_xx = selector1.xpath('//text()')
                    xx_aa = selector1.xpath('//a/text()')
                    output = set(xx_xx_xx) - set(xx_aa)
                    for x in output:
                        abs = re.findall('(.*mp4|.*mkv|.*720P)', x)
                        abs_url = ''
                        if abs:
                            for abs_single in abs:
                                abs_single_text = abs_single.replace('｜', '').replace(u'（', '')
                                # print abs_url, abs_single_text, content
                                values = (subject, url, category_name, abs_url, abs_single_text, content)
                                sql6 = 'INSERT INTO cn163_download_info (subject,url,category_name,download_url,download_name,content) VALUES ("%s","%s","%s","%s","%s","%s")' % values
                                mysql_dao.execute(sql6)
                                print sql6

        if len(xx) % 2 == 0:
            print u'偶数'
            for t in range(1, len(xx)):
                xx_xx = '<strong>' + xx[t]
                selector1 = etree.HTML(xx_xx)
                contents = selector1.xpath('//strong/text()')
                if len(contents) > 0:
                    content = contents[0]
                    # print content
                downloads = selector1.xpath('//a')
                for download in downloads:
                    download_urls = download.xpath('@href')
                    if download_urls:
                        download_url = download_urls[0]
                    download_names = download.xpath('text()')
                    if download_names:
                        download_name = download_names[0]
                    # print download_url, download_name,content
                    values = (subject, url, category_name, download_url, download_name, content)
                    sql7 = 'INSERT INTO cn163_download_info (subject,url,category_name,download_url,download_name,content) VALUES ("%s","%s","%s","%s","%s","%s")' % values
                    mysql_dao.execute(sql7)
                    print sql7


                xx_xx_xx = selector1.xpath('//text()')
                xx_aa = selector1.xpath('//a/text()')
                output = set(xx_xx_xx) - set(xx_aa)
                for x in output:
                    abs = re.findall('(.*mp4|.*mkv|.*720P)', x)
                    abs_url = ''
                    if abs:
                        for abs_single in abs:
                            abs_single_text = abs_single.replace('｜', '').replace(u'（', '')
                            # print abs_url, abs_single_text, content
                            values = (subject, url, category_name, abs_url, abs_single_text, content)
                            sql8 = 'INSERT INTO cn163_download_info (subject,url,category_name,download_url,download_name,content) VALUES ("%s","%s","%s","%s","%s","%s")' % values
                            mysql_dao.execute(sql8)
                            print sql8


if __name__ == '__main__':
    sql = 'SELECT `subject`,`single_url`,`category_name` FROM all_thread_list'
    res = mysql_dao.execute(sql)
    # print res
    for (subject,url,category_name) in res:
        print subject,url,category_name
        get_download_info(subject, url, category_name)






