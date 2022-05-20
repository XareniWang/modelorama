from elasticsearch import Elasticsearch
from elasticsearch import helpers

import common as common

es = Elasticsearch("localhost:9200")

def bulk_cities(cities):
    actions = [
    {
        "_index": common.INDEX_NAME,
        "_source": city
    }
    for city in cities
    ]
    helpers.bulk(es, actions)

def search(q, lat, long):
    body = common.make_body_es(q, lat, long)
    resp = es.search(index=common.INDEX_NAME, body=body)
    return resp
