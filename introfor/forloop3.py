#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Printing dictionary data stored as lists to the screen"""


# this is the data we want to loop across
# it is a list containing 3 dictionaries
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


for farm in farms:
    print(farm.get("name", "Unknown"), end=":\n")

    for agri in farm.get("agriculture"):
        print("  -", agri)







