import scrapy
from think_tank.items import ThinkTankItem
from think_tank.common_utils import start_item, parse_item


class ChaThamHouseSpider(scrapy.Spider):
    urls_data = start_item.get_url('chathamhouse')
    name = urls_data['tag']
    allowed_domains = [urls_data['site']]
    start_urls = urls_data['url']
    item = ThinkTankItem()

    def parse(self, response):
        get_second_navi = response.url + '?page=0'
        yield scrapy.Request(get_second_navi, callback=self.parse_second_navi)

    def parse_second_navi(self, response):
        """
        二级导航类型
        :param response:分类导航详情
        """
        # print(response.url)
        classify_urls = response.xpath('//div[@class="view-content"]//a/@href').extract()
        for classify_url in classify_urls:
            classify_detail_url = response.urljoin(classify_url)

            yield scrapy.Request(classify_detail_url, callback=self.parse_latest__detail)
        total_page = response.xpath('//li[contains(@class,"pager-next")]/a/@href').extract_first()
        if total_page:
            next_page = response.urljoin(total_page)
            yield scrapy.Request(next_page, callback=self.parse_second_navi)

    def parse_latest__detail(self, response):

        # 最新事件
        fragment0 = response.xpath(
            '//div[contains(@class,"view-section_index_auto_content_listing-default")]').extract()
        if fragment0:
            fragment0_url = response.url + '#fragment-0'
            yield scrapy.Request(fragment0_url, callback=self.parse_fragment0, dont_filter=True)
        # 以往事件
        fragment3 = response.xpath(
            '//div[contains(@class,"view-section_index_auto_content_listing-block_2")]').extract()
        if fragment3:
            fragment3_url = response.url + '#fragment-3'
            yield scrapy.Request(fragment3_url, callback=self.parse_fragment3, dont_filter=True)
        # 影音
        fragment4 = response.xpath(
            '//div[contains(@class,"view-section_index_auto_content_listing_audio_and_video-default")]').extract()
        if fragment4:
            fragment4_url = response.url + '#fragment-4'
            yield scrapy.Request(fragment4_url, callback=self.parse_fragment4, dont_filter=True)
        #

    def parse_fragment0(self, response):
        #     """
        #     解析三级导航第一列最新事件
        #     :param response: 页面链接
        #     :return:
        #     """
        base_classify_urls = response.xpath(
            '//div[contains(@class,"view-section_index_auto_content_listing-default")]')
        classify_latest_urls = base_classify_urls.xpath('./div/a//@href').extract()
        if classify_latest_urls:
            for classify_latest_url in classify_latest_urls:
                classify_latest = response.urljoin(classify_latest_url)
                yield scrapy.Request(classify_latest, callback=self.parse_page_detail, dont_filter=True)

        next_pager = base_classify_urls.xpath(
            './/li[contains(@class,"pager-next")]/a/@href').extract_first()
        if next_pager:
            next_page = response.urljoin(next_pager)
            yield scrapy.Request(next_page, callback=self.parse_fragment0)

    def parse_fragment3(self, response):
        base_fragment3_url = response.xpath(
            '//div[contains(@class,"view-section_index_auto_content_listing-block_3")]')
        classify_past_urls = base_fragment3_url.xpath('./div/a//@href').extract()
        if classify_past_urls:
            for classify_past_url in classify_past_urls:
                classify_past = response.urljoin(classify_past_url)
                yield scrapy.Request(classify_past, callback=self.parse_page_detail, dont_filter=True)

        next_pager = base_fragment3_url.xpath(
            './/li[contains(@class,"pager-next")]/a/@href').extract_first()
        if next_pager:
            next_page = response.urljoin(next_pager)
            yield scrapy.Request(next_page, callback=self.parse_fragment3)

    def parse_fragment4(self, response):
        base_fragment4_url = response.xpath(
            '//div[contains(@class,"view-section_index_auto_content_listing_audio_and_video-default")]')
        classify_past_urls = base_fragment4_url.xpath('./div/a/@href').extract()
        if classify_past_urls:
            for classify_past_url in classify_past_urls:
                classify_past = response.urljoin(classify_past_url)
                yield scrapy.Request(classify_past, callback=self.parse_page_detail, dont_filter=True)

        next_pager = response.xpath(
            '//div[@id="fragment-4"]//li[contains(@class,"pager-next")]/a/@href').extract_first()
        if next_pager:
            next_page = response.urljoin(next_pager)
            yield scrapy.Request(next_page, callback=self.parse_fragment4)

    def parse_page_detail(self, response):

        content_by_xpath = parse_item.parse_response(self.urls_data['tag'], response)
        # 对非解析获取的字段赋值
        parse_item.processing_data(content_by_xpath)
        data = parse_item.parse_common_field(response, content_by_xpath, self.urls_data['site'])
        item = ThinkTankItem()
        item['data'] = data
        item['site'] = self.urls_data['site']
        item['tag'] = self.urls_data['tag']
        yield item
