import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import MAIN_DOC_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [MAIN_DOC_URL]
    start_urls = [f'https://{url}/' for url in allowed_domains]

    def parse(self, response):
        pep_links = response.css(
            'section#numerical-index a::attr(href)'
        ).extract()
        pep_links = list(set(pep_links[1:]))
        pep_links.sort()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number = response.css('.breadcrumbs li:nth-child(3)::text').get()
        name = response.css('h1.page-title::text').get()
        status = response.css('dd abbr::text').get()
        data = {
            'number': int(number.replace('PEP ', '')),
            'name': name[name.find('–') + 2:],
            'status': status,
        }
        yield PepParseItem(data)

    def start_requests(self):
        return [scrapy.Request(url, callback=self.parse)
                for url in self.start_urls]
