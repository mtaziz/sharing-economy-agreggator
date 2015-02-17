# -*- coding: utf-8 -*-

# Scrapy settings for drivy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'drivy'

SPIDER_MODULES = ['drivy.spiders']
NEWSPIDER_MODULE = 'drivy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'drivy (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['drivy.pipelines.DrivyPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zilok (+http://www.yourdomain.com)'

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port':'5432',
	'username': 'postgres',
	'password': 'lifemaker1989',
	'database': 'scrape'
}