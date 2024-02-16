import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        numerical_index_section = response.css('section#numerical-index')
        pep_links = numerical_index_section.css('a::attr(href)').extract()
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
