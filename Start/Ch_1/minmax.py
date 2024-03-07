# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json
import os
print(f"current dir: {os.getcwd()}")


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value
print(f"The min value is: {min(values)}")
print(f"The min string is: {min(strings)}")

# TODO: The max() function finds the maximum value
print(f"The max value is: {max(values)}")
print(f"The max string is: {max(strings)}")

 
# TODO: define a custom "key" function to extract a data field
print(f"The max string is: {max(strings, key = len)}")
print(f"The min string is: {min(strings, key = len)}")

# TODO: open the data file and load the JSON

with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print(data['metadata']['title'])
print(len(data['features'])) 

def get_magnitude(data_item):
    magnitude = (data_item.get('properties',{}).get('mag',0))
    if magnitude is None: 
        magnitude = 0
    return float(magnitude)

print(min(data['features'],key=get_magnitude))
print(max(data['features'],key=get_magnitude))