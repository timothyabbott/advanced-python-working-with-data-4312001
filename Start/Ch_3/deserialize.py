# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint
result = []

# read the contents of a CSV file into an object structure
with open('largequakes.csv','r') as csv_for_reading:
    reader = csv.reader(csv_for_reading)
    sniffer = csv.Sniffer()
    sample = csv_for_reading.read(1024)
    csv_for_reading.seek(0)

    if sniffer.has_header(sample=sample):
        next(reader)
    for row in reader:
       result.append({
          "place": row[0],
          "magnitude": row[1],
          "date": row[2],
          "link": row[3]
       })
        


# TODO: open the CSV file for reading


pprint.pp(result)
