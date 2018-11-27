XPAHT_DATA = [
    {
        'id': 1,
        'site': 'brookings.edu',
        'tag': 'brookings',
        'xpath': [
            # 标题
            {'title': '//div[@class="headline-wrapper"]//h1//text()'},
            # 作者
            {'author': '//span[@class="names"]/a//text()'},
            # 内容
            {'content': '//div[contains(@class,"post-body")]/p//text()'},
            # 发布时间
            {'publish_time': '//time[@class="date"]//text()'},
            # 文章注释
            {'foot_note': '//section[@class="endnotes"]/div/ol/li//text()'},
            # 音频链接
            {'audio_url': '//div[contains(@class,"past-event-secondary-wrapper")]//article[3]/a/@href'},
            # 视频链接
            {'video_url': '//div[@class="vid-wrapper"]//@src'},
            # 相关领域/主题
            {'topics': '//section[@class="related-topics"]/div/ul/li//text()'},
            # 图片链接
            {'images_url': ['//div[@class="image-wrapper"]/img//@data-src',
                            '//div[contains(@class,"post-body")]//p//img/@src',
                            '//div[contains(@class,"post-body")]/div/img/@data-src',
                            ]},
            # 书籍说明
            {'book_info': '/html/body/div[2]/header/div/div[2]/h2//text()'},
            # 会议地址
            {'address': '//div[@itemprop="location"]//h4//text()'},
            # 网站logo
            {'logo': '/html/head/link[3]/@href'},
            # svg数据
            {'svg_data_urls': '//figure[@class="simplechart-widget"]/@data-url'}

        ]
    },
    {
        'id': 2,
        'site': 'brookings.edu',
        'tag': 'brookings_experts',
        'xpath': [
            # 专家头像
            {'expert_icon': '//div[@class="expert-image"]/img/@data-src'},
            # 专家名称
            {'expert_name': '//div[@class="expert-info"]/h1/text()'},
            # 专家说明
            {'expert_info': '//div[@class="expert-grid"]//font/text()'},
            # 专家详情
            {'expert_detail': '//div[contains(@class,"expert-intro-text ")]/p/text()'},
            # 专家简历
            {'expertCV': '//div[contains(@class,"download")]/ul/li[1]/a/@href'},
            # 网站logo
            {'logo': '/html/head/link[3]/@href'},
        ]
    },
    {
        'id': '3',
        'site': 'brookings.edu',
        'tag': 'brookings_about',
        'xpath': [
            # 内容
            {'content': '//div[contains(@class,"post-body")]/p//text()'},
            {'logo': '/html/head/link[3]/@href'},
        ]
    },
    {
        'id': 4,
        'site': 'rand.org',
        'tag': 'rand',
        'xpath': [
            # 标题
            {'title': '//div[@id="content"]//h1//text()'},
            # 图标
            {'logo': '//meta[@property="og:image"]/@content'},
            # 内容
            {'content': ['//div[@id="srch"]//p[@class=""]//text()',
                         '//div[@class="body-text"]//p//text()',
                         '//div[@id="onebio_overview"]//text()',
                         '//div[contains(@class,"product-main")]/*[not(self::section)]//text()',
                         ]},
            # 发布时间
            {'publish_time': [
                '//div[@class="eight columns"]//p[@class="publish-online"]//text()',
                '//*[@id="page-content"]/div[1]/div//p[@class="date"]//text()',
                '//*[@id="page-content"]//div[@class="newsicon"]/p[2]//text()'
            ]},
            # 图片链接
            {'images_url': ['//div[@class="cover-image"]/a[@id="look-inside"]/@href',
                            '//div[@class="section"]/a/@href',
                            ]
             },
            # 书籍说明
            {'book_info': '//div[@id="content"]//h2[@class="subtitle"]//text()'},
            # 视频链接
            {'video_url': '//div[@id="content"]//video/source[@type="video/mp4"]/@src'},
            # 视频内容
            {'video_content': '//div[@id="srch"]//p[@class=""]//text()'},
            # 相关话题
            {'topics': [
                '//div[@id="content"]//ul[@class="related-topics"]/li[position() > 1]//text()',
                '//aside/ul/li/a//text()',
                '//div[@class="four columns"]//li[@class="related"]//text()',

            ]},
            # 作者
            {'author': '//*[@id="page-content"]//p[@class="authors"]//a//text()'},
            # 出版物详情
            {'book_detail': '//aside[@class="document-details"]//ul/li//text()'},

            # 出版物链接
            {'book_url': [
                '//div[@class="cover-image"]/a[@id="look-inside"]/@href',
                '//div[@class="section"]/a/@href',
            ]},
            # 专家头像
            {'expert_ icon': '//div[@class="basic-info"]/img/@src'},
            # 专家名称
            {'expert_name': '//div[@id="content"]//h1//text()'},
            # 专家简介
            {'expert_info': '//div[@class="basic-info"]/div//text()'},
            # 专家详情
            {'expert_detail': '//div[@id="onebio_overview"]//text()'},
            # 专家简历
            {'expertDV': '//ul[contains(@class,"printable-info")]//a[@class="pdf"]/@href'}

        ]
    },
    {
        'id': 5,
        'site': 'chathamhouse.org',
        'tag': 'chathamhouse',
        'xpath': [
            # 标题
            {'title': '//section[contains(@class,"page__section__main")]//h1//text()'},
            # 作者/参与者
            {'author': '//div[@class="group-authors"]//text()'},
            # 内容
            {'content': '//div[contains(@class,"rich-text")]//text()'},
            # 发布时间
            {'publish_time': '//div[contains(@class,"date")]/span//text()'},
            # 文章注释
            {'foot_note': '//section[@class="endnotes"]/div/ol/li//text()'},
            # 音频链接
            {'audio_url': '//div[contains(@class,"past-event-secondary-wrapper")]//article[3]/a/@href'},
            # 视频链接
            {'video_url': '//div[@class="file"]//video/@src'},
            # 相关领域/主题
            {'topics': '//div[contains(@class,"projects")]/div//text()'},
            # 图片链接
            {'images_url': ['//div[@class="image-wrapper"]/img//@data-src',
                            '//div[contains(@class,"post-body")]//p//img/@src',
                            '//div[contains(@class,"post-body")]/div/img/@data-src',
                            ]},
            # 书籍说明
            {'book_info': '/html/body/div[2]/header/div/div[2]/h2//text()'},
            # 会议地址
            {'address': '//div[contains(@class,"meta--location")]//text()'},
            # 网站logo
            {'logo': '//link[@rel="shortcut icon"]/@href'},
            # 地理位置
            {'regions': '//div[contains(@class,"regions")]/div//text()'},

        ]
    },
    {
        'id': '6',
        'site': 'heritage.org',
        'tag': 'heritage',
        'xpath': [
            # 标题
            {'title': '//div[@id="block-mainpagecontent"]//h1//text()'},
            # 作者/参与者
            {'author': '//div[contains(@class,"contributors-list")]//text()'},
            # 内容
            {'content': [
                '//div[contains(@class,"body-copy")]//text()',
                '//section[contains(@class,"body-copy")]//text()'
            ]},
            # 文章要点
            {'content_key': '//div[contains(@class,"key-takeaways")]//p//text()'},
            # 文章详情
            {'content_detail': '//div[@id="block-mainpagecontent"]//div[@class="article-general-info"]/a/@href'},
            # 发布时间
            {'publish_time': '//div[@id="block-mainpagecontent"]//div[@class="article-general-info"]//text()'},
            # 文章注释
            {'foot_note': '//div[contains(@class,"references")]/div//text()'},
            # 音频链接
            {'audio_url': ''},
            # 视频链接
            {'video_url': ''},
            # 相关领域/主题
            {'topics': ''},
            # 图片链接
            {'images_url': '//div[contains(@class,body-copy)]//p//img/@src'},
            # 书籍说明
            {'book_info': ''},
            # 会议地址
            {'address': ''},
            # 网站logo
            {'logo': '//link[@rel="icon"]/@href'},
            # 专家头像
            {'expert_ icon': '//div[contains(@class,"card__photo")]/@style'},
            # 专家名称
            {'expert_name': '//div[@id="block-mainpagecontent"]//h1//text()'},
            # 专家简介
            {'expert_info': '//h2[contains(@class,"expert-title")]//text()'},
            # 专家详情
            {'expert_detail': '//div[contains(@class,"expert-bio-body")]//text()'},
            # 专家简历
            {'expertDV': ''},
            # 专家领域
            {'expert_topics': '//div[contains(@class,"areas-expertise")]//text()'}
        ]
    }
]
