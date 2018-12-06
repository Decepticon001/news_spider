# -*- coding: utf-8 -*-
import datetime
import hashlib
import time
import scrapy
import redis
from find_news.items import FindNewsItem
from util.get_img_to_local import replace_src
from util.get_time import Get_time
from find_news import settings
import re


"""
    
"""
class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['tech.qq.com']
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    d = date.split("-")
    # start_urls = ['http://tech.qq.com/l/201803/scroll_28.htm']
    start_urls = ['http://tech.qq.com/l/%s%s/scroll_%s.htm'%(d[0],d[1],d[2])]
    # def __init__(self):
    #     try:
    #         self.r = redis.Redis(host='localhost', password = '',port=6379, db=0)
    #     except:
    #         # print('redis链接异常')
    #         pass




    def more_info(self,response):
        try:
            # print(response.meta['item'])
            ge = Get_time()
            item = response.meta['item']
            if response.xpath("//span[@class='a_time']/text()"):
                time = response.xpath("//span[@class='a_time']/text()").extract_first().split(' ')[0]
            else:
                pass
            keywords = response.xpath("//span[@class='a_catalog']/a/text()").extract_first()
            item['News_Dt'] = time+' '+ge.Get_Time()
            item['Keywords']=keywords
            if item['Keywords'] is None:
                item['Keywords'] = '互联网'
            item['Abstract'] = None
            item['Author'] = response.xpath("//span[@class='a_source']/text()").extract_first()
            if item['Author'] is None:
                item['Author'] = response.xpath("//span[@class='a_source']/a/text()").extract_first()
            h1 = response.xpath("//h1").extract_first()
            article = response.xpath("//div[@id='Cnt-Main-Article-QQ']").extract_first()
            imgurl = response.xpath("//p[@align='center']/img/@src").extract()
            content =settings.HTML%("95%",h1,item['Author'],item['News_Dt'][:-4],article)
            content.replace("\\t", '')
            content.replace("\\n", '')
            # content = replace_src(content)
            # item['Content'] = content.replace("localhost","47.104.73.227")
            item['Content'] = content
            rule = r'src="(.*?)"'
            src_list = re.compile(rule, re.I).findall(item['Content'])
            if len(src_list)>4:
                item['Image_URL1'] = src_list[0]
                item['Image_URL2'] = src_list[1]
                item['Image_URL3'] = src_list[2]
                item['Image_URL4'] = src_list[3]
            elif len(imgurl)==3:
                item['Image_URL1'] = src_list[0]
                item['Image_URL2'] = src_list[1]
                item['Image_URL3'] = src_list[2]
                item['Image_URL4'] = None
            elif len(imgurl)==2:
                item['Image_URL1'] = src_list[0]
                item['Image_URL2'] = src_list[1]
                item['Image_URL3'] = None
                item['Image_URL4'] = None
            elif len(imgurl)==1:
                item['Image_URL1'] = src_list[0]
                item['Image_URL2'] = None
                item['Image_URL3'] = None
                item['Image_URL4'] = None
            else:
                item['Image_URL1'] = None
                item['Image_URL2'] = None
                item['Image_URL3'] = None
                item['Image_URL4'] = None
            item['Update_Tm'] = str(datetime.datetime.now())[:-3]
            yield item
        except:
            pass


    def parse(self, response):
        for u in response.xpath("//div[@class='mod newslist']/ul/li/a"):
            item = FindNewsItem()
            url = u.xpath("@href").extract_first()
            title = u.xpath("text()").extract_first()
            item['URL'] = url
            item['News_Title'] = title
            yield scrapy.Request(url, meta={'item': item}, callback=self.more_info)
            # sha1 = hashlib.sha1()
            # sha1.update(title.encode())
            # hashRs = sha1.hexdigest()
            # if self.r.sadd("tenxun",hashRs):
            #     item['URL'] = url
            #     item['News_Title'] = title
            #     yield scrapy.Request(url, meta={'item': item}, callback=self.more_info)
            # else:
            #     continue


        nextpage = response.xpath("//a[@class='f12']/@href").extract_first()
        if nextpage:
            yield scrapy.Request(nextpage,callback=self.parse)

