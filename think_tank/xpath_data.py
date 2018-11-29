XPAHT_DATA = [
    {
        'id': 1,
        'site': 'brookings.edu',
        'tag': 'brookings',
        'xpath': [
            # 当前链接
            {'primary_site': ''},
            # 爬取时间
            {'create_time': ''},
            # sha1指纹
            {'finger_print': ''},
            # 网站名称
            {'site_name': ''},
            # 主题
            {'topics': ''},
            # 标题
            {'title': '//div[@class="headline-wrapper"]//h1//text()'},
            # 作者
            {'author': '//span[@class="names"]/a//text()'},
            # 发布时间
            {'publish_time': '//time[@class="date"]//text()'},
            # 地址
            {'address': '//div[@itemprop="location"]//h4//text()'},
            # 文章说明
            {'content_info': '/html/body/div[2]/header/div/div[2]/h2//text()'},
            # 文章内容
            {'content': '//div[contains(@class,"post-body")]/p//text()'},
            # 文章注释
            {'content_annotation': '//section[@class="endnotes"]/div/ol/li//text()'},
            # 相关领域
            {'related_field': '//section[@class="related-topics"]/div/ul/li//text()'},
            # 地理位置
            {'regions': ''},
            # 文章pdf
            {'content_download': '//div[contains(@class,"download")]/ul/li[1]/a/@href'},
            # 图片链接
            {'image_url': [
                '//div[@class="image-wrapper"]/img//@data-src',
                '//div[contains(@class,"post-body")]//p//img/@src',
                '//div[contains(@class,"post-body")]/div/img/@data-src',
            ]},
            # 音频链接
            {'audio_url': '//div[contains(@class,"past-event-secondary-wrapper")]//article[3]/a/@href'},
            # 视频链接
            {'video_url': '//div[@class="vid-wrapper"]//@src'},
            # 网站logo
            {'logo': '/html/head/link[3]/@href'},
            # svg数据链接
            {'svg_url': '//figure[@class="simplechart-widget"]/@data-url'},
            # svg数据
            {'svg_data': ''},
            # 文章pdf
            {'content_download': ''},
            # 专家头像
            {'expert_icon': '//div[@class="expert-image"]/img/@data-src'},
            # 专家名称
            {'expert_name': '//div[@class="expert-info"]/h1/text()'},
            # 专家简介
            {'expert_info': '//div[@class="expert-grid"]//font/text()'},
            # 专家详情
            {'expert_detail': '//div[contains(@class,"expert-intro-text ")]/p/text()'},
            # 专家简历
            {'expert_dv': '//div[contains(@class,"download")]/ul/li[1]/a/@href'},
            # 专家领域
            {'expert_topics': ''},

        ]
    },
    {
        'id': 2,
        'site': 'rand.org',
        'tag': 'rand',
        'xpath': [
            # 当前链接
            {'primary_site': ''},
            # 爬取时间
            {'create_time': ''},
            # sha1指纹
            {'finger_print': ''},
            # 网站名称
            {'site_name': ''},
            # 主题
            {'topics': ''},
            # 标题
            {'title': '//div[@id="content"]//h1//text()'},
            # 作者
            {'author': '//*[@id="page-content"]//p[@class="authors"]//a//text()'},
            # 发布时间
            {'publish_time': [
                '//div[@class="eight columns"]//p[@class="publish-online"]//text()',
                '//*[@id="page-content"]/div[1]/div//p[@class="date"]//text()',
                '//*[@id="page-content"]//div[@class="newsicon"]/p[2]//text()'
            ]},
            # 地址
            {'address': ''},
            # 文章说明
            {'content_info': '//div[@id="content"]//h2[@class="subtitle"]//text()'},
            # 文章内容
            {'content': ['//div[@id="srch"]//p[@class=""]//text()',
                         '//div[@class="body-text"]//p//text()',
                         '//div[@id="onebio_overview"]//text()',
                         '//div[contains(@class,"product-main")]/*[not(self::section)]//text()',
                         '//aside[@class="document-details"]//ul/li//text()'
                         ]},
            # 文章注释
            {'content_annotation': ''},
            # 相关领域
            {'related_field': [
                '//div[@id="content"]//ul[@class="related-topics"]/li[position() > 1]//text()',
                '//aside/ul/li/a//text()',
                '//div[@class="four columns"]//li[@class="related"]//text()',

            ]},
            # 地理位置
            {'regions': ''},
            # 图片链接
            {'image_url': ['//div[@class="cover-image"]/a[@id="look-inside"]/@href',
                           '//div[@class="section"]/a/@href',
                           ]},
            # 音频链接
            {'audio_url': ''},
            # 视频链接
            {'video_url': '//div[@id="content"]//video/source[@type="video/mp4"]/@src'},
            # 网站logo
            {'logo': '//meta[@property="og:image"]/@content'},
            # svg数据链接
            {'svg_url': ''},
            # svg数据
            {'svg_data': ''},
            # 文章pdf
            {'content_download': [
                '//div[@class="cover-image"]/a[@id="look-inside"]/@href',
                '//div[@class="section"]/a/@href',
            ]},
            # 专家头像
            {'expert_icon': '//div[@class="basic-info"]/img/@src'},
            # 专家名称
            {'expert_name': '//div[@id="content"]//h1//text()'},
            # 专家简介
            {'expert_info': '//div[@class="basic-info"]/div//text()'},
            # 专家详情
            {'expert_detail': '//div[@id="onebio_overview"]//text()'},
            # 专家简历
            {'expert_dv': '//ul[contains(@class,"printable-info")]//a[@class="pdf"]/@href'},
            # 专家领域
            {'expert_topics': ''},

        ]
    },
    {
        'id': 3,
        'site': 'chathamhouse.org',
        'tag': 'chathamhouse',
        'xpath': [
            # 当前链接
            {'primary_site': ''},
            # 爬取时间
            {'create_time': ''},
            # sha1指纹
            {'finger_print': ''},
            # 网站名称
            {'site_name': ''},
            # 主题
            {'topics': ''},
            # 标题
            {'title': '//section[contains(@class,"page__section__main")]//h1//text()'},
            # 作者
            {'author': '//div[@class="group-authors"]//text()'},
            # 发布时间
            {'publish_time': '//div[contains(@class,"date")]/span//text()'},
            # 地址
            {'address': '//div[contains(@class,"meta--location")]//text()'},
            # 文章说明
            {'content_info': '/html/body/div[2]/header/div/div[2]/h2//text()'},
            # 文章内容
            {'content': '//div[contains(@class,"rich-text")]//text()'},
            # 文章注释
            {'content_annotation': '//section[@class="endnotes"]/div/ol/li//text()'},
            # 相关领域
            {'related_field': '//div[contains(@class,"projects")]/div//text()'},
            # 地理位置
            {'regions': '//div[contains(@class,"regions")]/div//text()'},
            # 图片链接
            {'image_url': ['//div[@class="image-wrapper"]/img//@data-src',
                           '//div[contains(@class,"post-body")]//p//img/@src',
                           '//div[contains(@class,"post-body")]/div/img/@data-src',
                           ]},
            # 音频链接
            {'audio_url': '//div[contains(@class,"past-event-secondary-wrapper")]//article[3]/a/@href'},
            # 视频链接
            {'video_url': '//div[@class="file"]//video/@src'},
            # 网站logo
            {'logo': '//link[@rel="shortcut icon"]/@href'},
            # svg数据链接
            {'svg_url': ''},
            # svg数据
            {'svg_data': ''},
            # 文章pdf
            {'content_download': ''},
            # 专家头像
            {'expert_icon': ''},
            # 专家名称
            {'expert_name': ''},
            # 专家简介
            {'expert_info': ''},
            # 专家详情
            {'expert_detail': ''},
            # 专家简历
            {'expert_dv': ''},
            # 专家领域
            {'expert_topics': ''},

        ]
    },
    {
        'id': 4,
        'site': 'heritage.org',
        'tag': 'heritage',
        'xpath': [
            # 当前链接
            {'primary_site': ''},
            # 爬取时间
            {'create_time': ''},
            # sha1指纹
            {'finger_print': ''},
            # 网站名称
            {'site_name': ''},
            # 主题
            {'topics': ''},
            # 标题
            {'title': '//div[@id="block-mainpagecontent"]//h1//text()'},
            # 作者
            {'author': '//div[contains(@class,"contributors-list")]//text()'},
            # 发布时间
            {'publish_time': '//div[@id="block-mainpagecontent"]//div[@class="article-general-info"]//text()'},
            # 地址
            {'address': ''},
            # 文章说明
            {'content_info': '//div[contains(@class,"key-takeaways")]//p//text()'},
            # 文章内容
            {'content': [
                '//div[contains(@class,"body-copy")]//text()',
                '//section[contains(@class,"body-copy")]//text()',
            ]},
            # 文章注释
            {'content_annotation': '//div[contains(@class,"references")]/div//text()'},
            # 相关领域
            {'related_field': ''},
            # 地理位置
            {'regions': ''},
            # 图片链接
            {'image_url': '//div[contains(@class,body-copy)]//p//img/@src'},
            # 音频链接
            {'audio_url': ''},
            # 视频链接
            {'video_url': ''},
            # 网站logo
            {'logo': '//link[@rel="icon"]/@href'},
            # svg数据链接
            {'svg_url': ''},
            # svg数据
            {'svg_data': ''},
            # 文章pdf
            {'content_download': '//div[@id="block-mainpagecontent"]//div[@class="article-general-info"]/a/@href'},
            # 专家头像
            {'expert_icon': '//div[contains(@class,"card__photo")]/@style'},
            # 专家名称
            {'expert_name': '//div[@id="block-mainpagecontent"]//h1//text()'},
            # 专家简介
            {'expert_info': '//h2[contains(@class,"expert-title")]//text()'},
            # 专家详情
            {'expert_detail': '//div[contains(@class,"expert-bio-body")]//text()'},
            # 专家简历
            {'expert_dv': ''},
            # 专家领域
            {'expert_topics': '//div[contains(@class,"areas-expertise")]//text()'},

        ]
    },
    {
        'id': 5,
        'site': 'carnegieendowment.org',
        'tag': 'carnegieendowment',
        'xpath': [
            # 当前链接
            {'primary_site': ''},
            # 爬取时间
            {'create_time': ''},
            # sha1指纹
            {'finger_print': ''},
            # 网站名称
            {'site_name': ''},
            # 主题
            {'topics': ''},
            # 标题
            {'title': '//div[contains(@class,"headline")]//h1//text()'},
            # 作者
            {'author': [
                '//div[contains(@class,"post-author")]//text()',
                '//div[contains(@class,"push-down")]/ul/li//a//text()',
                '//div[contains(@class,"large-text")]/ul//li/a/font//text()',
                '//div[@class="meta-heading"]//text()',
            ]},
            # 发布时间
            {'publish_time': [
                '//div[@class="component"]/ul/li[1]//text()',
                '//div[contains(@class,"post-date")]/ul/li[1]/text()',
                '//div[contains(@class,"pub-meta")]/ul/li//text()',
            ]},
            # 地址
            {'address': '//div[@class="component"]/ul/li[2]//text()'},
            # 文章说明
            {'content_info': [
                '//div[contains(@class,"zone-title__summary")]//text()',
                '//em[contains(@class,"large-text")]//text()',
                '//div[contains(@class,"largest-text")]//text()',
            ]},
            # 文章内容
            {'content': '//div[@class="article-body"]/p//text()'},
            # 文章注释
            {'content_annotation': ''},
            # 相关领域
            {'related_field': [
                '//div[contains(@class,"related-list")]//text()',
                '//div[contains(@class,"related-topics")]/ul/li//text()',
                '//div[@class="meta"]/div[2]//ul[contains(@class,"list-across")]/li//text()'
            ]},
            # 地理位置
            {'regions': ''},
            # 图片链接
            {'image_url': '//div[contains(@class,body-copy)]//p//img/@src'},
            # 音频链接
            {'audio_url': ''},
            # 视频链接
            {'video_url': ''},
            # 网站logo
            {'logo': ''},
            # svg数据链接
            {'svg_url': ''},
            # svg数据
            {'svg_data': ''},
            # 文章pdf
            {'content_download': ''},
            # 专家头像
            {'expert_icon': '//img[contains(@class,"show-expert-thumbnail")]/@src'},
            # 专家名称
            {'expert_name': '//h1[contains(@class,"roman-normal-bold")]//text()'},
            # 专家简介
            {'expert_info': '//div[contains(@class,"container-summary")]//text()'},
            # 专家详情
            {'expert_detail': '//div[contains(@class,"expert-bio-body")]//text()'},
            # 专家简历
            {'expert_dv': ''},
            # 专家领域
            {'expert_topics': '//div[@class="tab-content"]//ul/li//text()'},

        ]
    },
    {
        'id': 6,
        'site': 'bruegel.org',
        'tag': 'bruegel',
        'xpath': [
            # 当前链接
            {'primary_site': ''},
            # 爬取时间
            {'create_time': ''},
            # sha1指纹
            {'finger_print': ''},
            # 网站名称
            {'site_name': ''},
            # 主题
            {'topics': [
                '//p[contains(@class,"meta")]/span[3]//text()',
                '//article[contains(@class,"content event")]/div/p[2]/span[5]',
            ]},
            # 标题
            {'title': '//article[contains(@class,"content")]//h1//text()'},
            # 作者
            {'author': '//p[contains(@class,"meta")]//a[@rel="author"]//text()'},
            # 发布时间
            {'publish_time': [
                '//p[contains(@class,"meta")]/span[2]//text()',
                '//p[contains(@class,"meta")]//i[contains(@class,"fa-calendar")]/ancestor::span//text()',
            ]},
            # 地址
            {'address': '//div[@class="component"]/ul/li[2]//text()'},
            # 文章说明
            {'content_info': '//article[contains(@class,"content")]//p[contains(@class,"intro")]//text()'},
            # 文章内容
            {'content': '//div[contains(@class,"body")]/p//text()'},
            # 文章注释
            {'content_annotation': ''},
            # 相关领域
            {'related_field': '//div[@class="Tags"]//span[@class="Tags-name"]//text()'},
            # 地理位置
            {'regions': ''},
            # 图片链接
            {'image_url': ''},
            # 音频链接
            {'audio_url': ''},
            # 视频链接
            {'video_url': ''},
            # 网站logo
            {'logo': ''},
            # svg数据链接
            {'svg_url': ''},
            # svg数据
            {'svg_data': ''},
            # 文章pdf
            {'content_download': '//div[@class="publication"]/a[@class="download"]/@href'},
            # 专家头像
            {'expert_icon': ''},
            # 专家名称
            {'expert_name': ''},
            # 专家简介
            {'expert_info': ''},
            # 专家详情
            {'expert_detail': ''},
            # 专家简历
            {'expert_dv': ''},
            # 专家领域
            {'expert_topics': ''},

        ]
    },

]
