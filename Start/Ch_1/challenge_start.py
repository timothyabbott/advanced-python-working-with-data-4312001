# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

total_quakes = len(data['features'])
print (f'total total quakes {total_quakes}')

quakes_felt_by_100_or_morelist=list(
    filter(
        lambda q: (q['properties']['felt']is not None and 
                q['properties']['felt']>=100),data['features']
        )
    )

total_quakes_felt_by_100_or_more = len(quakes_felt_by_100_or_morelist)
print(f'Total quakes felt by at least 100 people: {total_quakes_felt_by_100_or_more}')


# should have used max here instead of sorted
quake_with_most_felt_reports = sorted(quakes_felt_by_100_or_morelist,key=lambda item:item['properties']['felt'] or 0,reverse=True )[0]
quake_with_most_felt_reports = max(quakes_felt_by_100_or_morelist,key=lambda item:item['properties']['felt'] or 0 )
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports

print (f'Most felt reports: {quake_with_most_felt_reports["properties"]["place"]}, reports: {quake_with_most_felt_reports["properties"]["felt"]}')

sorted_significant_quakes_top_ten = sorted(data['features'],key=lambda item:item['properties']['sig'] or 0,reverse=True )[:10]
print("The top 10 most significant events were:")

for q in sorted_significant_quakes_top_ten:
    print(f"Event: M {q['properties']['mag']} {q['properties']['place']} Signifiance: {q['properties']['sig']}")
