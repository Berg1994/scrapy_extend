import scrapy

from think_tank.items import ThinkTankItem
from think_tank.common_utils import start_item, parse_item


class BrookingsExpertsSpider(scrapy.Spider):
    urls_data = start_item.get_url('brookings_experts')
    name = urls_data['tag']
    allowed_domains = [urls_data['site']]
    start_urls = urls_data['url']

    def parse(self, response):
        """
        主页解析
        :param response:返回专家导航链接
        """
        experts_navi = response.xpath('//*[@id="menu-item-20631"]/a/@href').extract_first()
        experts__navi_url = response.urljoin(experts_navi)
        yield scrapy.Request(experts__navi_url, callback=self.parse_expert)

    def parse_expert(self, response):
        """
        专家页面解析
        :param response: 专家详情链接
        """

        experts_urls = response.xpath(
            '//div[@class="list-content"]/article/div[@class="expert-image"]/a/@href').extract()
        if experts_urls:
            for experts_url in experts_urls:
                yield scrapy.Request(experts_url, callback=self.parse_expert_detail)

            page = response.meta.get('page') if response.meta.get('page') else 1
            base_url = 'https://www.brookings.edu/experts/page/{}/'
            next_page = base_url.format(page)
            yield scrapy.Request(next_page, callback=self.parse_expert, meta={'page': page + 1})

    def parse_expert_detail(self, response):
        """
        解析专家详情
        """
        content_by_xpath = parse_item.parse_response(self.urls_data['tag'], response)
        # 对非解析获取的字段赋值
        data = parse_item.parse_common_field(response, content_by_xpath, self.urls_data['site'])
        item = ThinkTankItem()
        item['data'] = data
        item['site'] = self.urls_data['site']
        item['tag'] = self.urls_data['tag']
        yield item
