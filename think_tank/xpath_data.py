XPAHT_DATA = [
    {
        'id': 1,
        'site': 'brookings.edu',
        'tag': 'brookings',
        'xpath': [
            {'title': '//div[@class="headline-wrapper"]//h1//text()',
             'name': '标题'},
            {'author': '//span[@class="names"]/a//text()',
             'name': '作者'},
            {'content': '//div[contains(@class,"post-body")]/p//text()',
             'name': '内容'},
            {'publish_time': '//time[@class="date"]//text()',
             'name': '发布时间'},
            {'foot_note': '//section[@class="endnotes"]/div/ol/li//text()',
             'name': '文章脚注'},
            {'audio_url': '//div[contains(@class,"past-event-secondary-wrapper")]//article[3]/a/@href',
             'name': '音频链接'},
            {'video_url': '//div[@class="vid-wrapper"]//@src',
             'name': '视屏链接'},
            {'topic': '//section[@class="related-topics"]/div/ul/li//text()',
             'name': '相关领域'},
            {'images_url': '//div[@class="image-wrapper"]/img//@data-src | '
                           '//div[contains(@class,"post-body")]/div/img/@data-src',
             'name': '图片链接'},
            {'book_info': '/html/body/div[2]/header/div/div[2]/h2//text()',
             'name': '书籍简介'},
            {'address': '//div[@itemprop="location"]//h4//text()',
             'name': '活动地址'},
            {'logo': '/html/head/link[3]/@href',
             'name': '网站图标'},

        ]
    },
    {
        'id': 2,
        'site': 'brookings.edu',
        'tag': 'brookings_experts',
        'xpath': [
            {'expert_icon': '//div[@class="expert-image"]/img/@data-src',
             'name': '专家头像'},
            {'expert_name': '//div[@class="expert-info"]/h1/text()',
             'name': '专家名称'},
            {'expert_info': '//div[@class="expert-grid"]//font/text()',
             'name': '专家简介'},
            {'expertDetail': '//div[contains(@class,"expert-intro-text ")]/p/text()',
             'name': '专家详情'},
            {'expertCV': '//div[contains(@class,"download")]/ul/li[1]/a/@href',
             'name': '专家简历'},
            {'logo': '/html/head/link[3]/@href',
             'name': '网站图标'},
        ]
    },
    {
        'id': '3',
        'site': 'brookings.edu',
        'tag' : 'brookings_about',
        'xpath': [
            {'content': '//div[contains(@class,"post-body")]/p',
             'name': '关于网站详情'}
        ]
    },
    {
        'id': 4,
        'site': 'rand.org',
        'tag': 'brookings',
        'xpath': [
            {'title': '//div[@id="content"]//h1//text()'},
            {'content': ['//div[@id="srch"]//p[@class=""]//text()',
                         '//div[@class="body-text"]//p//text()',
                         '//div[@id="onebio_overview"]//text()',
                         '//div[@class="eight columns"]//p//text()',
                         '//div[contains(@class,"product-main")]//text()',
                         '//div[@id="srch"]//p[not(@class="linkbar")]//text()']},
            {'publish_time': '//div[@class="eight columns"]//p[@class="publish-online"]//text()'},
            {'images_url': '//div[@class="cover-image"]/a[@id="look-inside"]/@href,'
                           '//div[@class="section"]/a/@href'},
            {'book_info': '//div[@id="content"]//h2[@class="subtitle"]//text()'},

        ]
    }
]
