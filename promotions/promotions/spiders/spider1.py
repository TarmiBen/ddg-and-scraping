import csv
import scrapy

class Spider1(scrapy.Spider):
    name = "spider1"
    start_urls = []
    keyword = ""

    def __init__(self, keyword, urls):
        self.keyword = keyword
        self.start_urls = urls
        self.output_file = open("resultados.csv", mode="w", newline="", encoding="utf-8")
        self.csv_writer = csv.writer(self.output_file)

        self.csv_writer.writerow(["URL", "Ocurrencias"])

    def parse(self, response):

        text = response.text.lower()
        occurrences = text.count(self.keyword.lower())

        if occurrences > 0:
            print(f"Ocurrencias de '{self.keyword}' en {response.url}: {occurrences}")
            self.csv_writer.writerow([response.url, occurrences])
            yield {
                'url': response.url,
                'ocurrencias': occurrences
            }


    def close(self, reason):
        # Cierra el archivo CSV cuando el spider finaliza
        self.output_file.close()
        super().close(reason)