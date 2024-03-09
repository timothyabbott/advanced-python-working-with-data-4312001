 # Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter



# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
    types = [type['properties'].get('type','') for type in data['features']]

type_counter = Counter(types)
print(type_counter.items())
for k,v in type_counter.items():
    print(f'{k}: {v}')
