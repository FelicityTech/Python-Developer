from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ChocolatescraperPipeline:
    def process_item(self, item, spider):
        return item


class PriceToUSDPipeline:
    gbpToUsdRate = 1.3

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('price'):
            try:
                # Handle lists and convert to float
                price = adapter['price']
                if isinstance(price, list):
                    price = price[0]
                floatPrice = float(price)

                # Convert to USD
                adapter['price'] = floatPrice * self.gbpToUsdRate
                return item
            except (ValueError, TypeError):
                spider.logger.warning(f"Invalid price in item: {item}")
                raise DropItem(f"Invalid price in {item}")
        else:
            spider.logger.warning(f"Missing price in item: {item}")
            raise DropItem(f"Missing price in {item}")


class DuplicatesPipeline:
    def open_spider(self, spider):
        self.name_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        name = adapter['name'] 
        if isinstance(name, list):
            name = name[0]

        name = name.strip().lower()  # Normalize for case sensitivity

        if name in self.name_seen:
            spider.logger.warning(f"Duplicate item dropped: {item}")
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.name_seen.add(name)
            adapter['name'] = name
            return item
