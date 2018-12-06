# -*- coding: utf-8 -*-
import datetime
import re

import scrapy

from find_news.items import FindNewsItem
from find_news.settings import HTML
from util.drop_repeat import Drop_rep
from util.get_time import Get_time
from util.selenium_get_url import get_yidian_url


class YidianSpider(scrapy.Spider):
    name = 'yidian'
    dr = Drop_rep()
    allowed_domains = ['www.yidianzixun.com/channel/u8453']
    list = get_yidian_url()
    start_urls = list



    def parse(self, response):
        item = FindNewsItem()
        item['URL'] = response.url
        h1 = response.xpath("//h2").extract_first()
        item['News_Title'] = response.xpath("//h2/text()").extract_first()
        flag = self.dr.drop_re('yidianzixun', item['News_Title'])
        # if flag:
        ge = Get_time()
        News_Dt = response.xpath("//div[@class='meta']/span/text()").extract()
        if "小时前" in News_Dt:
            News_Dt = datetime.date.today()
        if "天前" in News_Dt:
            t = int(News_Dt[:1])
            News_Dt = News_Dt - datetime.timedelta(days=int(t))
        if News_Dt == "昨天":
            News_Dt = News_Dt - datetime.timedelta(days=1)
        item['News_Dt'] = News_Dt + ' ' + ge.Get_Time()
        item['Website_Id'] = ''
        item['Keywords'] = '互联网创业'
        item['Abstract'] = None
        item['Author'] = response.xpath("//a[@class='doc-source']/text()").extract_first()
        art = response.xpath("//div[@class='content-bd']").extract_first()
        content = HTML % ("95%", h1, item['Author'], item['News_Dt'].split(' ')[0], art)
        item['Content'] = content
        rule = r'src="(.*?)"'
        src_list = re.compile(rule, re.I).findall(item['Content'])
        for i in range(0, len(src_list)):
            if i == 4:
                break
            if src_list[i].startswith("//"):
                src_list[i] = "http:%s"%src_list[i]
            item['Image_URL%s' % str(i + 1)] = src_list[i]
        item['Original_Flag'] = '6'
        item["Tag_Group"] = ""
        item['Update_Tm'] = str(datetime.datetime.now())[:-3]
        yield item
        # else:
        #     return



# str(datetime.datetime.now())[:10]