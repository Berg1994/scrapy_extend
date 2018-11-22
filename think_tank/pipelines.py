# -*- coding: utf-8 -*-
import pymongo

from think_tank import settings


class ThinkTankPipeline(object):

    def __init__(self):
        self.mongodb_port = settings.MONGODB_HOST
        self.mongodb_host = settings.MONGODB_POST
        self.mongodb_db = settings.MONGODB_DB

        conn = pymongo.MongoClient(host=self.mongodb_port,
                                   port=self.mongodb_host)

        self.db = conn[self.mongodb_db]

    def process_item(self, item, spider):
        if spider.name == item['tag']:
            collcetions = self.db[item['tag']]
            collcetions.update({'finger_print': item['data']['finger_print']}, {'$set': item['data']}, True)

        return item
