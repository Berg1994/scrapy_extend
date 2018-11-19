import hashlib
import re
import time

import pymongo

from think_tank import xpath_data
from think_tank import settings


class Parse_xpath(object):

    def __init__(self):
        self.mongo_host = settings.MONGODB_HOST
        self.mongo_port = settings.MONGODB_POST
        self.mongo_db = settings.MONGODB_DB
        self.mongo_collection = settings.MONGODB_COLLECTIONS_XPATH_PARSE

        self.conn = pymongo.MongoClient(host=self.mongo_host,
                                        port=self.mongo_port)
        self.db = self.conn[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    def save_xpath_data(self):
        for xpath in xpath_data.XPAHT_DATA:
            self.collection.update_one({'id': xpath['id']}, {'$set': xpath}, True)

    def get_xpath_data(self, tag):
        res = self.collection.find_one({'tag': tag})
        return res

    def parse_response(self, tag, response):
        result = self.get_xpath_data(tag)
        data = {}
        for xpath_field in result['xpath']:
            for k, v in xpath_field.items():
                if isinstance(v, list):
                    for value in v:
                        ret = response.xpath(value).extarct()
                        if ret:
                            data[k] = self.parse_text(ret).strip()
                        else:
                            data[k] = ""
                else:
                    ret = response.xpath(v).extract()
                    if ret:
                        data[k] = self.parse_text(ret).strip()
                    else:
                        data[k] = ""
        return data

    def parse_common_field(self, response, data: dict, tag):
        data['primary_site'] = response.url
        data['org_name'] = tag
        data['create_time'] = time.time()
        data['finger_print'] = self.create_fingerprint(response.url)

        return data

    def parse_text(self, items):
        """
        对文本内容中的换行空格替换
        :param items: 节点获取的文本列表
        :return: 文本字符串
        """
        str_items = ''.join(items).strip()
        str_content = re.sub(r'\r|\n|\t\xa0', '', str_items)
        return str_content

    def create_fingerprint(self, url):
        hash_sha1 = hashlib.sha1(url.encode('utf8'))
        return hash_sha1.hexdigest()
