import json
import logging
import time

from elasticsearch import Elasticsearch


class ElasticSearchHandler(logging.Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.es = Elasticsearch("http://elasticsearch:9200")

    def emit(self, record):
        log_entry = {
            'timestamp': time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            'level': record.levelname,
        }
        log_entry.update(json.loads(self.format(record)))

        self.es.index(index=self.get_index_name(), document=log_entry)

    def get_index_name(self):
        return f'log_{time.strftime("%Y_%m_%d")}'