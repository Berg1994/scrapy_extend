import scrapy
from think_tank.items import ThinkTankItem
from think_tank.common_utils import start_item, parse_item


class CarnegieendowmentSpider(scrapy.Spider):
    urls_data = start_item.get_url('carnegieendowment')
    name = urls_data['tag']
    # allowed_domains = [urls_data['site']]
    start_urls = urls_data['url']

    def parse(self, response):

        base_url = 'https://carnegieendowment.org/search/?qry=&center='
        yield scrapy.Request(base_url, callback=self.parse_all_urls)

    def parse_all_urls(self, response):
        page_content_urls = response.xpath(
            '//div[contains(@class,"foreground")]//ul//li[@class="clearfix"]/h4/a/@href').extract()
        for page_content_url in page_content_urls:
            yield scrapy.Request(url=response.urljoin(page_content_url), callback=self.parse_page_detail)
        next_page = response.xpath('//a[contains(@class,"page-links__next")]/@href').extract_first()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse_all_urls)

    def parse_page_detail(self, response):
        content_by_xpath = parse_item.parse_response(self.urls_data['tag'], response)
        comment = content_by_xpath['comment_author']
        if comment:
            pass
        parse_item.processing_data(content_by_xpath)
        # 对非解析获取的字段赋值
        data = parse_item.parse_common_field(response, content_by_xpath, self.urls_data['site'])
        item = ThinkTankItem()
        item['data'] = data
        item['site'] = self.urls_data['site']
        item['tag'] = self.urls_data['tag']
        yield item
