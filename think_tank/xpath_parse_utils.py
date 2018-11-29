import hashlib
import json
import re
import time

import requests
import pymongo

from think_tank import xpath_data
from think_tank import settings


class Parse_xpath(object):

    def __init__(self):
        self.mongo_host = settings.MONGODB_HOST
        self.mongo_port = settings.MONGODB_POST
        self.mongo_db = settings.XPATH_MONGODB_DB
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
                print('%s------------------------------------> 保存成功' % xpath['tag'])
            print('保存完成')
        except Exception as e:
            print(e.args)
            print('保存失败')

    def get_xpath_data(self, site):
        """
        获取对应网站xpath解析数据
        :param site: 网站名称/标识
        :return: xpath数据
        """
        res = self.collection.find_one({'site': site})
        return res

    def parse_response(self, site, response):
        result = self.get_xpath_data(site)

        data = {}
        for xpath_field in result['xpath']:
            for k, v in xpath_field.items():
                if isinstance(v, list):
                    for value in v:
                        try:
                            ret = response.xpath(value).extract()
                            if ret:
                                # data[k] = (self.parse_text(ret).strip())
                                data[k] = ret
                        except:
                            data['error_url'] = response.url
                elif isinstance(v, str):
                    try:
                        ret = response.xpath(v).extract()
                        if not ret:
                            data[k] = ""
                        else:
                            # data[k] = self.parse_text(ret).strip()
                            data[k] = ret
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
        data['site_name'] = tag
        # 爬取时间
        data['create_time'] = time.time()
        # 指纹
        data['finger_print'] = self.create_fingerprint(response.url)
        # 内容分类
        try:
            if data['topics'] == "":
                data['topics'] = response.url.split('/')[3]
        except:
            data['topics'] = response.url

        return data

    def parse_svg_url(self, svg_urls):
        """
        解析brookings页面中svg图
        :param site: 网站名称/标识
        :param response: 页面响应
        :return: svg接口数据
        """
        svg_data_list = []
        for svg_url in svg_urls:
            svg_data = json.loads(requests.get(svg_url).text)
            svg_data_list.append(svg_data)
        return svg_data_list

    def parse_expert_DV(self, response, dv_url):
        """
        对于rand中专家简历链接进行拼接
        :param dv_url: 专家简历链接参数
        :return: 完整专家简历链接
        """
        if dv_url:
            base_url = response.url.split('/')[2]
            return base_url + dv_url
        return dv_url

    def processing_data(self, data):
        for k, v in data.items():
            if k == 'content':
                data[k] = self.parse_text(data[k])
            if k == 'address':
                data[k] = self.parse_text(data[k])
            if k == 'content_download':
                if data[k]:
                    data['expert_dv'] = ''
            if k == 'expert_name':
                if data[k]:
                    data['title'] = ''
            if k == 'expert_detail':
                if data[k]:
                    data['content'] = ''
        return data



    def parse_text(self, items):
        """
        对文本内容中的换行空格替换
        :param items: 节点获取的文本列表
        :return: 文本字符串
        """
        content = ''
        for ele in items:
            ele_str = re.sub(r'\r|\n|\t|\xa0', '', ele)
            content += ele_str + ' '
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
