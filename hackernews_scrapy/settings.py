import sys
import os


sys.path.append(os.path.join(os.path.dirname(os.getcwd()), "hackernews_scrapy"))

os.environ['DJANGO_SETTINGS_MODULE'] = 'lobsters_django.settings'

BOT_NAME = 'hackernews_scrapy'

SPIDER_MODULES = ['hackernews_scrapy.spiders']
NEWSPIDER_MODULE = 'hackernews_scrapy.spiders'

DOWNLOAD_DELAY = 2

DEPTH_LIMIT = 10

MIN_ARTICLE_LENGTH = 500

ITEM_PIPELINES = [
    'hackernews_scrapy.pipelines.DropSelfPostsPipeline',
    'hackernews_scrapy.pipelines.ExtractArticlePipeline',
    'hackernews_scrapy.pipelines.DropShortArticlesPipeline',
    'hackernews_scrapy.pipelines.SentimentPipeline'
]
