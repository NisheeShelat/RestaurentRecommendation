import requests
import json
overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
area["ISO3166-2"="US-CO"][admin_level=4];
(node["amenity"="restaurant"](area);
 way["amenity"="restaurant"](area);
 rel["amenity"="restaurant"](area);
);
out center;
"""
response = requests.get(overpass_url, params={'data': overpass_query})

data = response.json()
lst = list()
# count=0
# for dat in data['elements']:

#     for key,value in dat['tags'].items():
#         if (key == "addr:city" and value=="Boulder"):
#             for k,v in dat['tags'].items():
#                 if (k == "cuisine" and v=="asian"):
#                     # print(dat['id'])
#                     for ke,va in dat['tags'].items():
#                         if (ke == 'addr:street' and va=="Broadway"):
#                             lst.append(dat['id'])
#                             count+=1
#print("list",lst)
ctr=0
# for id in lst:
#     for dat in data['elements']:
       

#         for ki,vi in dat.items():
#             #print("key",ki,"value",vi)
#             if (ki == 'id' and vi==id):
#                 for key, val in dat['tags'].items():
#                     if key=="name":
#                         print(val)



                    # print(key)
                    
            
            # print(len(key))
print("Final")
for dat in data['elements']:
    for key,value in dat['tags'].items():
        print(key,value)