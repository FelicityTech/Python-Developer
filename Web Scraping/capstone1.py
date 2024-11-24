# parse method
def parse(self, response):
  # Extracted course titles
  crs_titles = response.xpath('//h4[contains(@class, "block__title")]/text()').extract()
  # Extracted course descriptions
  crs_descrs = response.xpath('//p[contains(@class, "block__description")]/text()').extract()
  # Fill in the dictionary: it is the spider output
  for crs_title, crs_descr in zip(crs_titles, crs_descrs):
    dc_dict[crs_title] = crs_descr