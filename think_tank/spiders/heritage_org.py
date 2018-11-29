import scrapy
from think_tank.items import ThinkTankItem
from think_tank.common_utils import start_item, parse_item


class HeritageSpider(scrapy.Spider):
    urls_data = start_item.get_url('heritage')
    name = urls_data['tag']
    allowed_domains = [urls_data['site']]
    start_urls = urls_data['url']

    def parse(self, response):
        """
        获取首页文章链接，解析所有页面链接
        :return:页面链接
        """
        # 翻页基础链接
        base_url = 'https://www.heritage.org/search?contains=&type=All&date_offset=&range_start=&range_end=&page={}'
        # 网站基础链接
        site_base_url = 'https://www.heritage.org'
        # 页面链接
        page_urls = response.xpath('//div[@class="views-row"]/section/div/a/@href').extract()
        for page_url in page_urls:
            yield scrapy.Request(site_base_url + page_url, callback=self.parse_page_detail)

        total_page = response.xpath('//li[contains(@class,"pager__item--last")]/a/@href').extract_first().split('=')[-1]
        for page in range(1, int(total_page) + 1):
            yield scrapy.Request(base_url.format(page), callback=self.parse_all_urls,
                                 meta={'site_base_url': site_base_url})

    def parse_all_urls(self, response):
        """
        获取所有页面下链接
        :return: 返回当前页面下链接
        """
        site_base_url = response.meta.get('site_base_url')
        page_urls = response.xpath('//div[@class="views-row"]/section/div/a/@href').extract()
        for page_url in page_urls:
            yield scrapy.Request(site_base_url + page_url, callback=self.parse_page_detail)

    def parse_page_detail(self, response):
        """
        解析页面详情
        """
        content_by_xpath = parse_item.parse_response(self.urls_data['tag'], response)
        # 对非解析获取的字段赋值
        parse_item.processing_data(content_by_xpath)
        data = parse_item.parse_common_field(response, content_by_xpath, self.urls_data['site'])
        item = ThinkTankItem()
        item['data'] = data
        item['site'] = self.urls_data['site']
        item['tag'] = self.urls_data['tag']
        yield item
