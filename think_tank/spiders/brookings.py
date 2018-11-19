# -*- coding: utf-8 -*-
import scrapy

from think_tank.items import ThinkTankItem
from think_tank.start_urls_utils import StartUrls
from think_tank.xpath_parse_utils import Parse_xpath


class BrookingsSpider(scrapy.Spider):
    url_item = StartUrls()
    urls_data = url_item.get_url('brookings.org')
    name = urls_data['site']
    # allowed_domains = urls_data['tag']
    start_urls = [urls_data['url']]

    def parse(self, response):
        """
        解析主页面
        :param response: 二级导航链接
        """
        second_navi_urls = response.xpath(
            '//div[@class="post-linear-list term-list topic-list-wrapper"][1]//ul/li/a/@href').extract()
        for second_navi_url in second_navi_urls:
            yield scrapy.Request(second_navi_url, callback=self.parse_second_navi, meta={'base_url': second_navi_url})

    def parse_second_navi(self, response):
        """
        解析二级导航
        :param response: 返回二级导航链接
        """
        base_url = response.meta.get('base_url')
        clssify_urls = base_url + 'page/{}/'.format(2)
        yield scrapy.Request(clssify_urls, callback=self.parse_topic_page, meta={'page': 2, 'url': base_url})

    def parse_topic_page(self, response):
        """
        解析主题
        :param response: 返回分类下每页链接
        """
        classify_page_urls = response.xpath(
            '//div[@class="list-content"]/article/a/@href | //div[@class="list-content"]/article/div/h4/a/@href'
        ).extract()
        if classify_page_urls:
            for page_url in classify_page_urls:
                yield scrapy.Request(page_url, callback=self.parse_page_detail, meta={'get_image': True})
        page = response.meta.get('page') + 1
        meta_url = response.meta.get('url')
        page_next = meta_url + 'page/{}/'.format(page)
        yield scrapy.Request(page_next, callback=self.parse_topic_page,
                             meta={'page': page, 'url': meta_url, })

    def parse_page_detail(self, response):
        parse_item = Parse_xpath()
        content_by_xpath = parse_item.parse_response(self.urls_data['tag'], response)
        data = parse_item.parse_common_field(response,content_by_xpath,self.urls_data['tag'])
        item = ThinkTankItem()
        item['data'] = data
        item['tag'] = self.urls_data['tag']
        item['site'] = self.urls_data['site']
        yield item