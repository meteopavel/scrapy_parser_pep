import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = defaultdict(int)
        self.timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    def process_item(self, item, spider):
        status = item.get('status')
        self.status_counts[status] += 1
        return item

    def close_spider(self, spider):
        filename = f'{BASE_DIR}/status_summary_{self.timestamp}.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ('Статус', 'Количество')
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            total_pep_documents = sum(self.status_counts.values())
            data_to_write = [
                (status, count) for status, count in self.status_counts.items()
            ] + [('Total', total_pep_documents)]
            writer.writerows([
                {'Статус': 'Статус', 'Количество': 'Количество'},
            ] + [
                {'Статус': status, 'Количество': count}
                for status, count in data_to_write
            ])
