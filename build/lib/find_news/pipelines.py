# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from config.db_connect import DBSession
from find_news import settings
from find_news.article import Article


class FindNewsPipeline(object):
    def __init__(self):
        try:
            self.session = DBSession()
            self.connect = pymysql.connect(
                host=settings.MYSQL_HOST,
                db=settings.MYSQL_DBNAME,
                user=settings.MYSQL_USER,
                passwd=settings.MYSQL_PASSWD,
                charset='utf8',
                use_unicode=True)
            self.cursor = self.connect.cursor();
        except:
            print("mysql链接异常")
            # pass
    def process_item(self, item, spider):
        try:
            if spider.name == 'news':
                self.cursor.execute('''insert into v_news (News_Title,News_Dt,Website_Id,URL,Keywords,Abstract,
                    Author,Content,Image_URL1,Image_URL2,Image_URL3,Image_URL4,Original_Flag,Tag_Group,Update_Tm)
                     values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                                    (item['News_Title'],item['News_Dt'],"5-3",item['URL'],
                                     item['Keywords'],item['Abstract'],
                                     item['Author'],item['Content'],item['Image_URL1'],
                                     item['Image_URL2'],item['Image_URL3'],item['Image_URL4'],'6',
                                     "I003",item["Update_Tm"]))
            elif spider.name == 'chyxx':
                article = Article(
                    News_Title=item['News_Title'],
                    News_Dt = item['News_Dt'],
                    Website_Id = item['Website_Id'],
                    URL = item['URL'],
                    Keywords = item['Keywords'],
                    Abstract = item['Abstract'],
                    Author = item['Author'],
                    Content = item['Content'],
                    Image_URL1 = item['Image_URL1'],
                    Image_URL2 = item['Image_URL2'],
                    Image_URL3 = item['Image_URL3'],
                    Image_URL4 = item['Image_URL4'],
                    Original_Flag = item['Original_Flag'],
                    Tag_Group = item["Tag_Group"],
                    Update_Tm = item["Update_Tm"]
                )
                self.session.add(article)
            self.session.commit()
            self.session.close()
            self.connect.commit()
        except Exception as e:
            print(e)
            # pass

