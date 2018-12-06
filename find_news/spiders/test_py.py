# -*- coding: utf-8 -*-
import scrapy


class TestPySpider(scrapy.Spider):
    name = 'test_py'
    allowed_domains = ['www.yidianzixun.com']
    start_urls = ['http://www.yidianzixun.com/channel/u8453']

    headers = {
        'Accept':'*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'wuid=958483495710434; wuid_createAt=2018-04-27%2010%3A20%3A08; UM_distinctid=16304e69236789-075da075e1c0c6-2d604637-3d10d-16304e6923766b; JSESSIONID=1d2b4017dff45741911f45cf38c31d63e64c7243fe38ea867a788c7593c929ee; Hm_lvt_15fafbae2b9b11d280c79eff3b840e45=1524795609,1525314662; Hm_lpvt_15fafbae2b9b11d280c79eff3b840e45=1525403697; CNZZDATA1255169715=1133494683-1525313927-%7C1525402038; cn_1255169715_dplus=%7B%22distinct_id%22%3A%20%2216304e69236789-075da075e1c0c6-2d604637-3d10d-16304e6923766b%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201525422704%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201525422704%7D%7D; weather_auth=2; captcha=s%3A727e21e668a1e44f7f8096675d5fd485.5kEs8FeRI35K7OkInM97fMM6UJyU3DiSiM4lcihjhMg; sptoken=Uhoy~U8%3AU9%3AU48261efeced332cc9f20413132c69381b0cfd133e5b4eb17c4e6b154cad55db0',
        'Host': 'www.yidianzixun.com',
        'Referer': 'http://www.yidianzixun.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    def parse(self, response):
        pass
