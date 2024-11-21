from scrapy import Selector

# Create a selector from the html (of a secret website)
sel = Selector( text=html )
css = "div.course-block > a"
print(how_many_elements(css))