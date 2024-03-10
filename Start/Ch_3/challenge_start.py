# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
    
top_40_events = sorted(data['features'],key= lambda feature:feature['properties']['sig'],reverse=True)[:40]
top_40_events_sorted_by_date = sorted(top_40_events,key=lambda feature:feature['properties']['time'],reverse=True)

header = ['Magnitude', 'Place', 'Felt Reports', 'Date','Google Map link']

with open('events.csv','w') as events_file:
    writer = csv.writer(events_file,delimiter=',')
    for event in top_40_events:
        writer.writerow([
            event['properties']['mag'],
            event['properties']['place'],
            event['properties']['felt'] if event['properties']['felt'] else '',
            str(datetime.date.fromtimestamp(event['properties']['time']/1000)),
            f"https://www.google.com/maps/@?api=1&map_action=map&center={event['geometry']['coordinates'][1]}%2C{event['geometry']['coordinates'][0]}&zoom=12&basemap=terrain"
        ])

