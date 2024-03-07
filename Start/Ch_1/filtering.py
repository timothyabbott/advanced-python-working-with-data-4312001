# Example file for Advanced Python: Working With Data by Joe Marini
# using the filter() function to filter a data set

import json


def filterEvens(x):
    # filters out even numbers and keeps odd numbers
    if x % 2 == 0:
        return False
    return True 


def filterUppers(x):
    # filters out upper-case letters and keeps lower case letters
    if x.isupper():
        return False
    return True


# # define some sample sequences to operate on
# nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
# chars = "abcDeFGHiJklmnoP"

# # TODO: use filter to remove items from a list
# odds = list(filter(lambda x:(x % 2),nums))
# print(odds)
# # this is how the tutorial suggests filtering
# odds = list(filter(filterEvens,nums))
# print(odds)

# # TODO: use filter on non-numeric sequence
# letters = list(filter(lambda z:(z.isupper()),chars))
# print(letters)

# Use the filter on our data - let's filter out all seismic events that were *not* quakes
# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

non_quakes = list(filter(lambda q: q['properties']['type']!='earthquake'),data['features'])
for non_quake in non_quakes:
    print(non_quake['properties']['type'])
