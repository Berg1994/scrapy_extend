import scrapy
from think_tank.items import ThinkTankItem
from think_tank.common_utils import start_item, parse_item


class RandOrgSpider(scrapy.Spider):
    urls_data = start_item.get_url('rand')
    name = urls_data['tag']
    allowed_domains = [urls_data['site']]
    start_urls = urls_data['url']

    def parse(self, response):
        """
        获取所有导航链接
        :param response: 链接
        """
        base_link = 'https://www.rand.org'
        result = response.xpath('//ul[@class="topic-list"]/li/ul/li/a/@href').extract()
        for url in result:
            classify_url = base_link + url
            yield scrapy.Request(url=classify_url, callback=self.parse_calssify)

    def parse_calssify(self, response):
        base_url = response.url
        page_url = base_url + '?page={}'.format(1)
        yield scrapy.Request(url=page_url, callback=self.parse_all_url, meta={'page': 1, 'url': base_url})

    def parse_all_url(self, response):
        """
        获取每页信息
        :param respones: 返回页面链接
        """

        res = response.xpath('//ul[@class="teasers list organic"]/li/div[2]/h3/a/@href').extract()
        if res:
            for detail_url in res:
                yield scrapy.Request(url=detail_url, callback=self.parse_page_detail)

            page = response.meta.get('page') + 1
            meta_url = response.meta.get('url')
            url = meta_url + '?page={}'.format(page)
            yield scrapy.Request(url=url, callback=self.parse_all_url, meta={'page': page, 'url': meta_url})

    def parse_page_detail(self, response):
        """
        解析页面详情
        :return: item
        """
        content_by_xpath = parse_item.parse_response(self.urls_data['tag'], response)
        # 对非解析获取的字段赋值
        data = parse_item.parse_common_field(response, content_by_xpath, self.urls_data['site'])
        item = ThinkTankItem()
        item['data'] = data
        item['site'] = self.urls_data['site']
        item['tag'] = self.urls_data['tag']
        yield item
