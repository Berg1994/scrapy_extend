import scrapy
from think_tank.items import ThinkTankItem
from think_tank.common_utils import start_item, parse_item


class BruegelSpdier(scrapy.Spider):
    urls_data = start_item.get_url('bruegel')
    name = urls_data['tag']
    allowed_domains = [urls_data['site']]
    start_urls = urls_data['url']

    def parse(self, response):
        page_content_urls = response.xpath('//div[@class="mdl-submenu"]/a[1]/@href').extract()
        if page_content_urls:
            for page_content_url in page_content_urls:
                yield scrapy.Request(page_content_url, callback=self.parse_page_detail)

            base_url = 'http://bruegel.org/?basefilter=all&s=&paged={}'
            if response.meta.get('page'):
                page = response.meta.get('page')
            else:
                page = 1
            yield scrapy.Request(url=base_url.format(page), callback=self.parse, meta={'page': page + 1})

    def parse_page_detail(self, response):

        content_by_xpath = parse_item.parse_response(self.urls_data['tag'], response)
        # 对非解析获取的字段赋值
        data = parse_item.parse_common_field(response, content_by_xpath, self.urls_data['site'])
        item = ThinkTankItem()
        item['data'] = data
        item['site'] = self.urls_data['site']
        item['tag'] = self.urls_data['tag']
        yield item
