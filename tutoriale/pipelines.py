# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import logging
import redis
import pymysql
import time as tm
from .utils.dateconvrt import cdate
from datetime import datetime
#-----------------items to json---------------------------------
#import json
#class TutorialPipeline(object):
#   def open_spider(self, spider):
#       self.file = open(spider.name + ".jl", "w")
#   def close_spider(self, spider):
#       self.file.close()
#   def process_item(self, item, spider):
#       line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#       self.file.write(line)
#       return item
#
#----------------items to mysql---------------------------------


class MysqlPipeline(object):
    def __init__(self, mysql_host, mysql_db, mysql_user, mysql_passwd):
        self.mysql_host = mysql_host
        self.mysql_db = mysql_db
        self.mysql_user = mysql_user
        self.mysql_passwd = mysql_passwd
        self.redis = redis.Redis(host='127.0.0.1',port=6379,db=0)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_host = crawler.settings.get('MYSQL_HOST'),
            mysql_db = crawler.settings.get('MYSQL_DB'),
            mysql_user = crawler.settings.get('MYSQL_USERNMAE'),
            mysql_passwd = crawler.settings.get('MYSQL_PASSWORD')
            )

    def open_spider(self, spider):
        self.con = pymysql.connect(host=self.mysql_host, user=self.mysql_user, password=self.mysql_passwd, db=self.mysql_db, charset='utf8')
        self.cursor = self.con.cursor()

    def close_spider(self, spider):
        self.con.close()

    def process_item(self, item, spider):
        sql = "INSERT INTO article(title, author, abstract, time, keywords, journal, getdate, link) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        if 'abstract' in item.keys() and item['abstract']:
            try:
                keywords=None
                if 'keywords' in item.keys():
                    keywords=item['keywords']
                getdate = tm.strftime('%Y-%m-%d', tm.localtime())
                time=cdate(item['time'])
                abstract=item['abstract']

                date_getdate=datetime.strptime(getdate, '%Y-%m-%d')
                date_time=datetime.strptime(time, '%Y-%m-%d')
                date_delta=abs(date_time-date_getdate)
                if date_delta.days < 31:
                    # fetch the latest article.
                    self.cursor.execute(sql, (item['title'], item['author'], abstract, time, keywords, item['journal'], getdate, item['link']))
                    self.redis.sadd('url',item['link'])
                    self.con.commit()
            except pymysql.err.IntegrityError as e:
                if "Duplicate entry" in str(e):
                    self.redis.sadd('url',item['link'])
                    raise DropItem('Dupelicate item:%s' % item['title'])
                else:
                    logging.error(str(e) + '!!!!!!!!!!!!!!!!!!!!!!!' + item['link'] + ' !!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except pymysql.err.Error as e:
                logging.error("!!!!!!!!!!!!!!!!!!!!!!!!!!!Mysql Error!!!!!!!!!!!!!!!!!!!!!!!%s>>>>%s---%s： %s" % (spider.name, item['journal'], item['link'], e))
                self.con.rollback()
            return item
        else:
            raise DropItem('No Abstract:%s>>>>%s' % (item['journal'], item['link']))
