import requests
import json

BBOX = ''' s="32.631279542388256" w="-117.40951538085938" n="32.85594120414512" e="-116.91307067871094" '''

QUERY_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<osm-script output="json" timeout="25">
  <!-- gather results -->
  <union>
    <!-- query part for: "amenity=restaurant and cuisine=mexican" -->
    <query type="node">
      <has-kv k="amenity" v="restaurant"/>
      <has-kv k="cuisine" v="mexican"/>
      <bbox-query %(bbox)s />
    </query>
    <query type="way">
      <has-kv k="amenity" v="restaurant"/>
      <has-kv k="cuisine" v="mexican"/>
      <bbox-query %(bbox)s />
    </query>
    <query type="relation">
      <has-kv k="amenity" v="restaurant"/>
      <has-kv k="cuisine" v="mexican"/>
      <bbox-query %(bbox)s />
    </query>
  </union>
  <print mode="body"/>
  <recurse type="down"/>
  <print mode="skeleton" order="quadtile"/>
</osm-script>'''%{"bbox":BBOX}

TARGET_URL = "http://overpass-api.de/api/interpreter"

def query_taco_restaurants():
    resp = requests.post(TARGET_URL,data={"data":QUERY_XML})
    if resp.status_code != 200:
        print(resp,resp.content)
    return resp.json()

if __name__=="__main__":
    obj = query_taco_restaurants()
    features = []
    for o in obj["elements"]:
        if "tags" in o and "name" in o["tags"] and "lon" in o:
            f = {
                "type":"Feature",
                "properties": dict( [(k,v) for k,v in o["tags"].items()] ),
                "geometry":{
                    "type": "Point",
                    "coordinates": [ o["lon"],o["lat"] ],
                }
            }
            features.append(f)  
    f = open("data/tacos.json","w")
    f.write(json.dumps(features,indent=1))
    f.close()
    print("Wrote %i features to tacos.json" % len(features) )


