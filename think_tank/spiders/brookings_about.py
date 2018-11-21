import scrapy

from think_tank.items import ThinkTankItem
from think_tank.common_utils import start_item, parse_item


class BrookingsAboutSpider(scrapy.Spider):
    urls_data = start_item.get_url('brookings_experts')
    name = urls_data['tag']
    allowed_domains = [urls_data['site']]
    start_urls = urls_data['url']

    def parse(self, response):
        """
        解析页面信息
        """
        content_by_xpath = parse_item.parse_response(self.urls_data['tag'], response)
        # 对非解析获取的字段赋值
        data = parse_item.parse_common_field(response, content_by_xpath, self.urls_data['site'])
        item = ThinkTankItem()
        item['data'] = data
        item['site'] = self.urls_data['site']
        item['tag'] = self.urls_data['tag']
        yield item
