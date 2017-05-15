#-*- coding:utf-8 -*-
from lxml import etree
import requests
from public.mysqlpooldao import MysqlDao
from public.headers import Headers
import re



mysql_dao = MysqlDao()

def get_single_url(lastpage,category_name,url):
    page = lastpage
    headers = Headers.get_headers()
    while True:
        if page <= 0:
            break
        target_url = url + 'page/' + str(page)+ '/'
        print '################'
        print target_url
        res = requests.get(target_url,headers=headers)
        wb_data = res.content
        selector = etree.HTML(wb_data)
        proxy_lists = selector.xpath('//div[@id="content"]/div[@class="entry_box"]')
        for proxy_list in proxy_lists:
            single_url = subject = pub_date = content_title = ''
            comment_num = total_num = 0
            single_urls = proxy_list.xpath('div[@class="archive_box"]/span[@class="archive_more"]/a/@href')
            if len(single_urls) > 0:
                single_url = single_urls[0]
                # print single_url

                headers = Headers.get_headers()
                res = requests.get(single_url, headers=headers)
                qwz = res.status_code
                if qwz == 200:
                    wb_data = res.content
                    selector = etree.HTML(wb_data)
                    contents = selector.xpath('//div[@id="entry"]/descendant::p/text()')
                    f = lambda x: x.strip()
                    contents_list = [f(x) for x in contents]
                    content = ' '.join(contents_list)
                    content = content.replace(u'《', '').replace(u'》', '')
                    # print content

                    res1 = requests.get(single_url, headers=headers)
                    wb_data1 = res1.content
                    selector1 = etree.HTML(wb_data1)
                    contents1 = selector1.xpath('//div[@id="entry"]/descendant::p/text()')
                    f = lambda x: x.strip()
                    contents_list1 = [f(x) for x in contents]
                    content1 = ' '.join(contents_list1)
                    content1 = content.replace(u'《', '').replace(u'》', '')
                    # print content
                    abstract1 = re.findall(u'(.*?)播出', content)
                    f = lambda x: x.strip()
                    content_list1 = [f(x) for x in abstract1]
                    content_title = ' '.join(content_list1).replace('"', '')


                    broadcast = type = area = actor = language = date = producer = othername = ''
                    broadcasts1 = re.findall(u'播出：(.*)', content)
                    if broadcasts1:
                        broadcast = broadcasts1[0].split(' ')[0]
                    # print broadcast
                    # return broadcast

                    types1 = re.findall(u'类 型：(.*)', content)
                    if types1:
                        # print types1[0]
                        type = types1[0].split(' ')[0]
                    else:
                        types2 = re.findall(u'类型：(.*)', content)
                        # print types2
                        if types2:
                            type = types2[0].split(' ')[0]
                    # print type
                    # return type

                    areas1 = re.findall(u'地区：(.*)', content)
                    if areas1:
                        area = areas1[0].split(' ')[0]
                    # print area
                    # return area


                    # actors1 = re.findall(u'主演: (.*)', content)
                    # if actors1:
                    #     actor = actors1[0].split(' ')[0]
                    # print actor
                    # return actor
                    content_1 = content.replace(u'，',' ').replace(u'：',':')
                    if content1:
                        cc = re.findall(u'主演:([\S\s]+?):', content_1)
                        dd = re.findall('([\s\S]+)\s\S+', cc[0])
                        actor = dd
                        # print dd


                    languages1 = re.findall(u'语言：(.*)', content)
                    if languages1:
                        language = languages1[0].split(' ')[0]
                    # print language
                    # return language

                    # dates1 = re.findall(u'首播:(.*)', content)
                    # if dates1:
                    #     date = dates1[0].split(' ')[0]
                    # else:
                    #     dates2 = re.findall(u'首播日期：(.*)', content)
                    #     if dates2:
                    #         date = dates2[0].split(' ')[0]
                    # print date
                    # return date

                    content2 = content.replace(u'：',':')
                    # print content2
                    ss = re.findall(u'[首播日期|首播]:([\S\s]+?):', content2)
                    if ss:
                        qq = re.findall('([\s\S]+)\s\S+', ss[0])
                        date = qq[0]
                        # print date





                    producers1 = re.findall(u'制作公司：(.*)', content)
                    if producers1:
                        producer = producers1[0].split(' ')[0]
                    # print producer
                    # return producer

                    othernames1 = re.findall(u'别名：(.*)', content)
                    if othernames1:
                        othername = othernames1[0].split(' ')[0]
                    # print othername
                    # return othername

                    # return  single_url,broadcast,type,area,actor,language,date,producer,othername
                    # print single_url, broadcast, type, area, actor, language, date, producer, othername


                # print content_title
            subjects = proxy_list.xpath('div[@class="archive_box"]/div[@class="archive_title_box"]/div[@class="archive_title"]/h2/a/text()')
            if len(subjects) > 0:
                subject = subjects[0]
                # print subject
            pub_dates = proxy_list.xpath('div[@class="archive_box"]/div[@class="archive_title_box"]/div[@class="archive_info"]/span[@class="date"]/text()')
            if len(pub_dates) > 0:
                pub_date = pub_dates[0].replace(u'年','-').replace(u'月','-').replace(u'日','')
                # print pub_date
            comment_nums = proxy_list.xpath('div[@class="archive_box"]/div[@class="archive_title_box"]/div[@class="archive_info"]/span[@class="comment"]/a/text()')
            if len(comment_nums) > 0:
                comment_num = comment_nums[0].replace(u'评论','').replace(u'条','').strip()
                # print comment_num
            total_nums = proxy_list.xpath('div[@class="archive_box"]/div[@class="archive_title_box"]/div[@class="archive_info"]/text()')
            if len(total_nums) > 0:
                total_num = total_nums[2].replace(u'共','').replace(u'字','').replace(u'⁄ ','').strip()
                # print total_num
            values = (subject,pub_date,comment_num,total_num,single_url,category_name,content_title,broadcast, type, area, actor, language, date, producer, othername)
            sql2  = 'INSERT ignore INTO `all_thread_list` (subject,pub_date,comment_num,total_num,single_url,category_name,content_title,broadcast, type, area, actor, language, date, producer, othername)  VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % values
            mysql_dao.execute(sql2)
            print sql2
        page = page - 1

def get_last_page(url):
    res = requests.get(url)
    wb_data = res.content
    selector = etree.HTML(wb_data)
    last_pages = selector.xpath('//div[@id="pagenavi"]/a[last()-1]/text()')
    if len(last_pages) > 0:
        last_page = int(last_pages[0])
        print last_page
    return last_page



if __name__ == '__main__':
    sql1 = 'SELECT `category_name`,`url` FROM `meiju_category_list`'
    res = mysql_dao.execute(sql1)
    for (category_name,url) in res:
        print category_name,url
        lastpage = get_last_page(url)
        get_single_url(lastpage,category_name,url)



