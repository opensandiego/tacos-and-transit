import requests
from urllib import parse
import json

YELP_KEYS = json.loads(open("yelp_keys.json").read())

# https://www.yelp.com/developers/documentation/v3/business_search

def get_taco_stands():
    base_url = "https://api.yelp.com/v3/businesses/search"
    params = {  
        "categories": "tacos",
        "location": "san diego, ca",
        "sort_by": "rating",
    }

    businesses = []
    def q(offset,businesses):
        print(".%i"%offset)
        headers = {"Authorization":"Bearer %s"%YELP_KEYS["api_key"]}
        response = requests.get(
            base_url,
            params,
            headers=headers
        )
        results = response.json()
        businesses += results["businesses"]
        if len(businesses) >= results["total"]:
            return None 
        return True

    i = 0
    while q(i,businesses) != None:
        i += 1 

    # Score
    transit_stop_coords = [t["geometry"]["coordinates"] for t in json.loads(open("data/transit_stops_datasd.json").read())]
    # CONSIDER boost based on stop_agency? Wheelchair  

    for b in businesses:
        # geojson likes long first..
        b_coord = [b["coordinates"]["longitude"],b["coordinates"]["latitude"]]
        # TODO score based on cumulative distance of nearby stops .. math maybe numpy?
        score = 1.0
        b["score"] = score

    for b in businesses:
        print(b["name"]),score

    print("%i taco shops" % len(businesses))
    f = open("tacos.json","w")
    f.write(json.dumps(businesses,indent=1))
    f.close()

if __name__=="__main__":
    get_taco_stands() 


