# Scrapy settings for dirbot project

SPIDER_MODULES = ['robot.spiders']
NEWSPIDER_MODULE = 'robot.spiders'
DEFAULT_ITEM_CLASS = 'robot.items.AdItem'

ITEM_PIPELINES = [
    'robot.pipelines.RequiredFieldsPipeline',
    'robot.pipelines.FilterWordsPipeline',
    'robot.pipelines.MySQLStorePipeline',
]

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'test'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'lifemaker1989'
