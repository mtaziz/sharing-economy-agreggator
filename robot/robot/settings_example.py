from scrapy import log

# Scrapy settings for dirbot project

SPIDER_MODULES = ['robot.spiders']
NEWSPIDER_MODULE = 'robot.spiders'
DEFAULT_ITEM_CLASS = 'robot.items.AdItem'

ITEM_PIPELINES = [
    'robot.pipelines.RequiredFieldsPipeline',
    'robot.pipelines.FilterWordsPipeline',
    'robot.pipelines.MySQLStorePipeline',
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline'
]

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'alterrefront'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'lifemaker1989'

ELASTICSEARCH_SERVER = 'localhost' # If not 'localhost' prepend 'http://'
ELASTICSEARCH_PORT = 9200 # If port 80 leave blank
ELASTICSEARCH_USERNAME = ''
ELASTICSEARCH_PASSWORD = ''
ELASTICSEARCH_INDEX = 'robot'
ELASTICSEARCH_TYPE = 'ads'
ELASTICSEARCH_UNIQ_KEY = 'url'
ELASTICSEARCH_LOG_LEVEL= log.DEBUG
