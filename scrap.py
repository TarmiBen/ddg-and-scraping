from duckduckgo_search import DDGS
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from promotions.promotions.spiders.spider1 import Spider1  #



query = "quarry jeans"
results = DDGS().text(query, max_results=5)
urls = [result['href'] for result in results]

process = CrawlerProcess(get_project_settings())

process.crawl(Spider1, keyword="look", urls=urls)

process.start()
