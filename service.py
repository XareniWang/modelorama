import elastic as elastic
import common as common

def search_cities(q, lat, long):
    found_cities_es = elastic.search(q, lat, long)
    hits = found_cities_es["hits"]["hits"]
    list_cities = list(map(common.response_cities, hits))
    return list_cities

def bulk_cities(cities):
    elastic.bulk_cities(cities)

