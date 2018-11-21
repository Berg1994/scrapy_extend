import hashlib
import json
import re
import time

import requests
import scrapy
import pymongo

from think_tank import xpath_data
from think_tank import settings
from think_tank.spiders import brookings


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
        """
        保存xpath解析数据
        """
        try:
            for xpath in xpath_data.XPAHT_DATA:
                self.collection.update_one({'id': xpath['id']}, {'$set': xpath}, True)
            print('保存成功')
        except:
            print('保存失败')

    def get_xpath_data(self, tag):
        """
        获取对应网站xpath解析数据
        :param site: 网站名称/标识
        :return: xpath数据
        """
        res = self.collection.find_one({'tag': tag})
        return res

    def parse_response(self, tag, response):
        result = self.get_xpath_data(tag)

        data = {}
        for xpath_field in result['xpath']:
            for k, v in xpath_field.items():
                if isinstance(v, list):
                    for value in v:
                        try:
                            ret = response.xpath(value).extract()
                            if ret:
                                data[k] = (self.parse_text(ret).split())


                        except:
                            data['error_url'] = response.url
                elif isinstance(v, str):
                    try:
                        ret = response.xpath(v).extract()
                        if not ret:
                            data[k] = ""
                        else:
                            data[k] = self.parse_text(ret).strip()
                    except:
                        data['error_url'] = response.url
        return data

    def parse_common_field(self, response, data: dict, tag):
        """
        非xpath解析字段处理
        :param response: 文章内容响应
        :param data: xpath解析内容
        :param site: 网站标识
        :return: 页面解析内容
        """
        # 当前页面链接
        data['primary_site'] = response.url
        # 网站名称
        data['org_name'] = tag
        # 爬取时间
        data['create_time'] = time.time()
        # 指纹
        data['finger_print'] = self.create_fingerprint(response.url)
        # 内容分类
        try:
            data['classify'] = response.url.split('/')[3]
        except:
            data['classify'] = response.url

        return data

    def parse_svg_url(self, svg_urls):
        """
        解析页面中svg图
        :param site: 网站名称/标识
        :param response: 页面响应
        :return: svg接口数据
        """
        svg_data_list = []
        for svg_url in svg_urls.split():
            svg_data = json.loads(requests.get(svg_url).text)
            svg_data_list.append(svg_data)
        return svg_data_list

    def parse_text(self, items):
        """
        对文本内容中的换行空格替换
        :param items: 节点获取的文本列表
        :return: 文本字符串
        """
        content = ''
        for ele in items:
            str = re.sub(r'\r|\n|\t|\xa0', '', ele)
            content += str + ' '
        return content.strip()

    def create_fingerprint(self, url):
        """
        生成链接摘要
        :param url: 当前页面链接
        :return: 链接摘要
        """
        hash_sha1 = hashlib.sha1(url.encode('utf8'))
        return hash_sha1.hexdigest()


def main():
    xpath = Parse_xpath()
    xpath.save_xpath_data()


if __name__ == '__main__':
    main()
