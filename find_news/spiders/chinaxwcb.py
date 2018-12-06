# -*- coding: utf-8 -*-
import datetime
import re
import scrapy
from find_news.items import FindNewsItem
from find_news.settings import HTML
from util.drop_repeat import Drop_rep
from util.get_time import Get_time


class ChinaxwcbSpider(scrapy.Spider):
    name = 'chinaxwcb'
    allowed_domains = ['www.chinaxwcb.com']
    dr = Drop_rep()
    start_urls = ['http://www.chinaxwcb.com/chuanmeipindao/node_425.htm']

    def more_info(self,response):
        item = response.meta['item']
        ge = Get_time()
        News_Dt = None
        try:
            News_Dt = response.xpath("//div[@class='info']/text()").extract_first().split(":")[3][1:11]
        except Exception as e:
            print(e)
        item['News_Dt'] = News_Dt + ' ' + ge.Get_Time()
        item['Website_Id'] = '5-9'
        item['Keywords'] = '媒体'
        Author = response.xpath("//div[@class='info']/text()").extract_first()
        Author = " ".join(Author.split())
        # print(Author)
        au = Author.split(' ')
        aut = ''
        for a in au:
            if '来源' in a:
                aut = a
        aut = aut.split(":")
        Author = aut[1]
        item['Author'] = Author
        h1 = response.xpath("//h1").extract_first()
        art = response.xpath("//div[@class='content']").extract()[1]
        content = HTML % ("95%",h1,item['Author'],item['News_Dt'].split(' ')[0],art)
        content = content.replace("\\r", '')
        content = content.replace("\\n", '')
        content = content.replace("\\t", '')
        content = content.replace("\\u3000", '')
        with open('1.html','w',encoding='utf-8') as f:
            f.write(content)
        item['Content'] = content
        item['Image_URL1'] = None
        item['Image_URL2'] = None
        item['Image_URL3'] = None
        item['Image_URL4'] = None
        rule = r'src="(.*?)"'
        src_list = re.compile(rule, re.I).findall(item['Content'])
        for i in range(0, len(src_list)):
            if i == 4:
                break
            if src_list[i].startswith(".."):
                src_list[i] = 'http://www.chinaxwcb.com/'+src_list[i][6:]
            item['Image_URL%s' % str(i + 1)] = src_list[i]
        item['Original_Flag'] = '6'
        item["Tag_Group"] = "I010"
        item['Update_Tm'] = str(datetime.datetime.now())[:-3]
        yield item

    def parse(self, response):
        for u in response.xpath("//div[@id='cmyw_list']/ul/li"):
            item = FindNewsItem()
            title = u.xpath("a/p/text()").extract_first()
            ul = u.xpath("a/@href").extract_first()
            url = response.urljoin(ul)
            Abstract = u.xpath("p[@class='news_content']/text()").extract_first()
            item['URL'] = url
            item['News_Title'] = title
            item['Abstract'] = Abstract
            yield scrapy.Request(url, meta={'item': item}, callback=self.more_info)
            # flag = self.dr.drop_re('finance_news', title)
            # if flag:
            #     item['URL'] = url
            #     item['News_Title'] = title
            #     item['Abstract'] = Abstract
            #     yield scrapy.Request(url, meta={'item': item}, callback=self.more_info)
            # else:
            #     continue
