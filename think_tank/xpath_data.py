XPAHT_DATA = [
    {
        'id': 1,
        'tag': 'brookings.org',
        'xpath': [
            {'title': '//div[@class="headline-wrapper"]//h1//text()'},
            {'author': '//span[@class="names"]/a//text()'},
            {'content': '//div[contains(@class,"post-body")]/p//text()'},
            {'publish_time': '//time[@class="date"]//text()'},
            {'images_url': '//div[@class="image-wrapper"]/img//@data-src | '
                          '//div[contains(@class,"post-body")]/div/img/@data-src'},
            {'book_info': '/html/body/div[2]/header/div/div[2]/h2//text()'},
            {'address': '//div[@itemprop="location"]//h4//text()'},
            {'audioUrl': '//div[contains(@class,"past-event-secondary-wrapper")]//article[3]/a/@href'},
            {'footNote': '//section[@class="endnotes"]/div/ol/li//text()'},
            {'expert_icon':'//div[@class="expert-image"]/img/@data-src'},
            {'expert_name':'//div[@class="expert-info"]/h1/text()'},
            {'expert_info':'//div[@class="expert-grid"]//font/text()'},
            {'expertDetail':'//div[contains(@class,"expert-intro-text ")]/p/text()'},
            {'expertCV':'//div[contains(@class,"download")]/ul/li[1]/a/@href'},
            {'logo':'/html/head/link[3]/@href'},
        ]
    },
    {
        'id':2,
        'tag':'rand.org',
        'xpath':[
            {'title':'//div[@id="content"]//h1//text()'},
            {'content':['//div[@id="srch"]//p[@class=""]//text()',
                        '//div[@class="body-text"]//p//text()',
                        '//div[@id="onebio_overview"]//text()',
                        '//div[@class="eight columns"]//p//text()',
                        '//div[contains(@class,"product-main")]//text()',
                        '//div[@id="srch"]//p[not(@class="linkbar")]//text()']},
            {'publish_time':'//div[@class="eight columns"]//p[@class="publish-online"]//text()'},
            {'images_url':'//div[@class="cover-image"]/a[@id="look-inside"]/@href,'
                          '//div[@class="section"]/a/@href'},
            {'book_info':'//div[@id="content"]//h2[@class="subtitle"]//text()'},

        ]
    }
]