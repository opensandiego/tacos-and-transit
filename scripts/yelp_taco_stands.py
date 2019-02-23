import requests
from urllib import parse
import json

try:
    YELP_KEYS = json.loads(open("yelp_keys.json").read())
except IOError:
    print("Please create a file called yelp_keys.json and add to it: {\"api_key\":\"<yourkey>\"}")

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

    features = []
    for b in businesses:
        b_coord = [b["coordinates"]["longitude"],b["coordinates"]["latitude"]]
        f = {
            "type":"Feature",
            "properties": {
                "name": b["name"],
                "amenity":"restaurant",
                "cuisine":"mexian",
            },
            "geometry": {
                "type":"Point",
                "coordinates": b_coord,
            }
        }
        features.append(f)

    f = open("data/tacos.json","w")
    f.write(json.dumps(features,indent=1))
    f.close()

if __name__=="__main__":
    get_taco_stands() 


