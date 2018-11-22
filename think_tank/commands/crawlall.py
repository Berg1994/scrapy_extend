# from scrapy.command import ScrapyCommand, UsageError
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.conf import arglist_to_dict
#
#
# class Command(ScrapyCommand):
#     requires_project = True
#
#     def syntax(self):
#         return '[options]'
#
#     def short_desc(self):
#         return 'Run all of the spiders'
#
#     def add_options(self, parser):
#         ScrapyCommand.add_options(self, parser)
#         parser.add_option("-a", dest="spargs", action="append", default=[], metavar="NAME=VALUE",
#                           help="set spider argument (may be repeated)")
#         parser.add_option("-o", "--output", metavar="FILE",
#                           help="dump scraped items into FILE (use - for stdout)")
#         parser.add_option("-t", "--output-format", metavar="FORMAT",
#                           help="format to use for dumping items with -o")
#
#     def process_options(self, args, opts):
#         ScrapyCommand.process_options(self, args, opts)
#         try:
#             opts.spargs = arglist_to_dict(opts.spargs)
#         except ValueError:
#             raise UsageError("Invalid -a value, use -a NAME=VALUE", print_help=False)
#
#     def run(self, args, opts):
#         spider_list = self.crawler_process.spiders.list()
#         for name in spider_list:
#             self.crawler_process.crawl(name, **opts.__dict__)
#         self.crawler_process.start()
