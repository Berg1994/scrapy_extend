import scrapy

from think_tank.items import ThinkTankItem
from think_tank.start_urls_utils import StartUrls
from think_tank.xpath_parse_utils import Parse_xpath


class BrookingsAboutSpider(scrapy.Spider):
    url_item = StartUrls()
    parse_item = Parse_xpath()
    urls_data = url_item.get_url('brookings_experts')
    name = urls_data['tag']
    allowed_domains = [urls_data['site']]
    start_urls = urls_data['url']

    def parse(self, response):
        """
        解析页面信息
        """
        content_by_xpath = self.parse_item.parse_response(self.urls_data['tag'], response)
        # 对非解析获取的字段赋值
        data = self.parse_item.parse_common_field(response, content_by_xpath, self.urls_data['site'])
        item = ThinkTankItem()
        item['data'] = data
        item['site'] = self.urls_data['site']
        item['tag'] = self.urls_data['tag']
        yield item
