BASE_DIR = 'results'
MAIN_DOC_URL = 'peps.python.org'

BOT_NAME = 'pep_parse'

SPIDER_MODULES = [f'{BOT_NAME}.spiders']
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}
