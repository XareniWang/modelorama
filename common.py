
INDEX_NAME = "cities"
LAT_SCALE = "10"
LONG_SCALE = "10"
LAT_DECAY = "0.5"
LONG_DECAY = "0.5"


def response_cities(city):
    source =  city["_source"]
    response = {
        "name": f'{source["name"]}, {source.get("admin1", "")}, {source["country"]}',
        "latitude": source["lat"],
        "longitude": source["long"],
        "score": city["_score"]
    }
    return response

def make_body_es(q, lat, long):
    body = {
        "query": {
            "function_score": {
                "score_mode": "multiply",
                "query": query_body(q),
                }
            }
        }
    
    if lat != None or long != None:
        functions = { "functions": [] }
        if lat != None:
            lat_function_body = functions_body("lat", lat, LAT_SCALE, LAT_DECAY)
            functions["functions"].append(lat_function_body)
        if long != None:
            long_function_body = functions_body("long", long, LONG_SCALE, LONG_DECAY)
            functions["functions"].append(long_function_body)
        body["query"]["function_score"] = {**body["query"]["function_score"], **functions}

    return body

def query_body(q):
    query_body = {
            "wildcard": {
                "name": f'*{q}*'
            }
        }
    
    return query_body

def functions_body(field, origin, scale, decay=0.5):
    functions_body = {
        "gauss": {
            field: {
                "origin": origin,
                "scale": scale,
                "decay": decay
                }
            }
        }
    return functions_body



