import csv
from collections import defaultdict
from datetime import datetime

BASE_DIR = 'results'


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
            writer.writeheader()
            total_pep_documents = sum(self.status_counts.values())
            for status, count in self.status_counts.items():
                writer.writerow({'Статус': status, 'Количество': count})
            writer.writerow(
                {'Статус': 'Total', 'Количество': total_pep_documents}
            )
