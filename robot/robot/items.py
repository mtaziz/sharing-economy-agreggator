from scrapy.item import Item, Field
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst


class AdItem(Item):
    title = Field()
    description = Field()
    url = Field()
    media = Field()
    location = Field()
    price = Field()
    period = Field()  
    source = Field()
    category = Field()
    
class AdLoader(XPathItemLoader):
    default_item_class = AdItem
    default_output_processor = TakeFirst()