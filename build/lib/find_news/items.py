# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    News_Title = scrapy.Field()
    News_Dt = scrapy.Field()
    Website_Id = scrapy.Field()
    URL = scrapy.Field()
    Keywords = scrapy.Field()
    Abstract = scrapy.Field()
    Author = scrapy.Field()
    Content = scrapy.Field()
    Image_URL1 = scrapy.Field()
    Image_URL2 = scrapy.Field()
    Image_URL3 = scrapy.Field()
    Image_URL4 = scrapy.Field()
    Original_Flag = scrapy.Field()
    # Original_Declare_Flag = scrapy.Field()
    # Auth_Flag = scrapy.Field()
    # Ad_Flag = scrapy.Field()
    Tag_Group = scrapy.Field()
    Update_Tm = scrapy.Field()

