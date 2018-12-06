# -*- coding: utf-8 -*-
import datetime
import re
import scrapy
from find_news.items import FindNewsItem
from find_news.settings import HTML
from util.drop_repeat import Drop_rep
from util.get_img_to_local import remote_to_local, replace_src
from util.get_time import Get_time


class FinanceSpider(scrapy.Spider):
    name = 'finance'
    dr = Drop_rep()
    allowed_domains = ['finance.qq.com']
    start_urls = ['http://finance.qq.com/gdyw.htm']
    headers={'Refere': 'http://finance.qq.com/gdyw.htm'}
    def get_news(self,response):
        item = response.meta['item']
        ge = Get_time()
        News_Dt = None
        try:
            News_Dt = response.xpath("//span[@class='a_time']/text()").extract_first().split(' ')[0]
        except Exception as e:
            print(e)
        item['News_Dt'] = News_Dt + ' ' + ge.Get_Time()
        item['Website_Id'] = '5-6'
        kw = response.xpath("//div[@class='hd qq_subTit2 clearfix']/div[@class='mark']/span/a/text()").extract()
        keyword = ''
        if kw:
            for k in kw:
                keyword = keyword+k+","
            item['Keywords'] = keyword
        else:
            item['Keywords'] = '财经'
        item['Abstract'] = None
        if response.xpath("//p[@class='titdd-Article']/text()").extract():
            Abstract = response.xpath("//p[@class='titdd-Article']/text()").extract()[1][1:]
            item['Abstract'] = Abstract
        Author = response.xpath("//span[@class='a_source']/a/text()").extract_first()
        if Author:
            item['Author'] = Author
        elif response.xpath("//span[@class='a_source']/text()").extract():
            item['Author'] = response.xpath("//span[@class='a_source']/text()").extract_first()
        h1 = response.xpath("//div[@class='hd']/h1").extract_first()
        art = response.xpath("//div[@class='Cnt-Main-Article-QQ']").extract_first()
        vido = response.xpath("//div[@class='rv-root-v2 rv-js-root']").extract()
        scrp = response.xpath("//script").extract()
        iframe = response.xpath("//iframe").extract()
        style = response.xpath("//style").extract()
        content = HTML % ("95%",h1,item['Author'],item['News_Dt'].split(' ')[0],art)
        content = content.replace("\\t", '')
        content = content.replace("\\n", '')
        for sty in style:
            content = content.replace(sty, '')
        for vi in vido:
            content = content.replace(vi,'')
        for sc in scrp:
            content = content.replace(sc,'')
        for ifra in iframe:
            content = content.replace(ifra,'')
        content = replace_src(content)
        item['Content'] = content.replace("localhost","47.104.73.227")
        # item['Content'] = content
        rule = r'src="(.*?)"'
        src_list = re.compile(rule, re.I).findall(item['Content'])
        r = 0
        if item['Image_URL1']:
            r = 1
        for i in range(r,len(src_list)):
            if i == 4:
                break
            if 'newsapp_match' in src_list[i][-1]:
                continue
            item['Image_URL%s'%str(i+1)] = src_list[i]
        item['Original_Flag'] = '6'
        item["Tag_Group"] = "I009"
        item['Update_Tm'] = str(datetime.datetime.now())[:-3]
        yield item

    def parse(self, response):
        for u in response.xpath("//div[@class='Q-tpWrap']"):
            item = FindNewsItem()
            url = response.urljoin(u.xpath("em/a/@href").extract_first())
            title = u.xpath("em/a/text()").extract_first()
            """
                测试用
            """
            # item['URL'] = url
            # item['News_Title'] = title
            # item['Image_URL1'] = None
            # item['Image_URL2'] = None
            # item['Image_URL3'] = None
            # item['Image_URL4'] = None
            # if u.xpath("a/img/@src").extract_first():
            #     img_src = u.xpath("a/img/@src").extract_first()
            #     # img_src = remote_to_local(img_src).replace("localhost","47.104.73.227")
            #     item['Image_URL1'] = img_src
            # yield scrapy.Request(url=url, headers={'Refere': 'http://finance.qq.com/gdyw.htm'},meta={'item': item}, callback=self.get_news)
            """
                测试
            """
            flag = self.dr.drop_re('finance_news',title)
            if flag:
                item['URL'] = url
                item['News_Title'] = title
                item['Image_URL1'] = None
                item['Image_URL2'] = None
                item['Image_URL3'] = None
                item['Image_URL4'] = None
                if u.xpath("a/img/@src").extract_first():
                    img_src = u.xpath("a/img/@src").extract_first()
                    img_src = remote_to_local(img_src).replace("localhost","47.104.73.227")
                    item['Image_URL1'] = img_src
                yield scrapy.Request(url=url,headers={'Refere': 'http://finance.qq.com/gdyw.htm'},meta={'item': item},callback=self.get_news)
            else:
                continue

            """
            
            """

        for i in range(2, 4):
            url = "http://finance.qq.com/c/gdyw_%s.htm" % str(i)
            yield scrapy.Request(url=url, headers={'Refere': 'http://finance.qq.com/gdyw.htm'}, callback=self.parse)