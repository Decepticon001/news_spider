# -*- coding: utf-8 -*-
import datetime
from find_news.items import FindNewsItem
import scrapy
from find_news.settings import HTML
from util.drop_repeat import Drop_rep
from util.get_time import Get_time
from util.replace_img import replace_img_src


class ChyxxSpider(scrapy.Spider):
    name = 'chyxx'
    allowed_domains = ['www.chyxx.com']
    start_urls = ['http://www.chyxx.com/industry/dianziyuanqijian/1.html']
    dr = Drop_rep()
    Headers = {
        'Referer':'http://www.chyxx.com/'
    }

    def get_info(self,response):
        item = response.meta['item']
        ge = Get_time()
        News_Dt = None
        try:
            News_Dt = response.xpath("//div[@class='info']/span/text()").extract_first()[0:10]
            News_Dt = News_Dt.replace("年", "-")
            News_Dt = News_Dt.replace("月", "-")
        except Exception as e:
            print(e)
        item['News_Dt'] = News_Dt + ' ' + ge.Get_Time()
        item['Website_Id'] = '5-5'
        item['Keywords'] = '电子元器件'
        item['Abstract'] = None
        item['Author'] = '中国产业信息'
        h1 = response.xpath("//h1").extract_first()
        tag = response.xpath("//div[@class='info']").extract_first()
        art =response.xpath("//div[@class='articleBody news-content']").extract_first()
        dele = response.xpath("//div[@class='articleBody news-content']/div[@class='content-weixin weixin-box clearfix']").extract_first()
        art = art.replace(dele,'')
        art = art.replace("<a","<span")
        content = HTML % ("95%", h1,item['Author'],item['News_Dt'][:-4],art)
        content = content.replace(r"\xa0", '')
        content = content.replace(r"\n", '')
        content = replace_img_src(content)
        item['Content'] = content
        item['Image_URL1'] = None
        item['Image_URL2'] = None
        item['Image_URL3'] = None
        item['Image_URL4'] = None
        img_list = response.xpath("//p[@style='text-align: center;']/img/@src").extract()
        for i in range(0,len(img_list)):
            if i == 4:
                break
            if img_list[i].startswith("/"):
                img_list[i] = "http://img.chyxx.com%s"%img_list[i]
            item['Image_URL%s'%str(i+1)] = img_list[i]
        item['Original_Flag'] = '6'
        item["Tag_Group"] = 'I0010402'
        item['Update_Tm'] = str(datetime.datetime.now())[:-3]
        yield item

    def parse(self, response):
        for u in response.xpath("//ul[@class='list']/li/a"):
            item = FindNewsItem()
            title = u.xpath("text()").extract_first()
            url = u.xpath("@href").extract_first()
            url = response.urljoin(url)
            item['URL'] = url
            item['News_Title'] = title
            yield scrapy.Request(url, headers={'Referer': 'http://www.chyxx.com/'}, meta={'item': item},
                                 callback=self.get_info)
            # flag = self.dr.drop_re("chyxx_news",title)
            # if flag:
            #     yield scrapy.Request(url,headers={'Referer':'http://www.chyxx.com/'}, meta={'item': item}, callback=self.get_info)
            # else:
            #     continue
        for i in range(1,4):
            url = "http://www.chyxx.com/industry/dianziyuanqijian/%s.html"%str(i)
            yield scrapy.Request(url=url,headers={'Referer':'http://www.chyxx.com/'},callback=self.parse)


