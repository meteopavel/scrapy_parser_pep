BASE_DIR = 'results'
MAIN_DOC_URL = 'peps.python.org'

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]


ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
