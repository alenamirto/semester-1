# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {"cocteau twins": "heaven or las vegas", 
         "blood orange": "coastal grooves",
         "jane taylor": "twinkle twinkle little star",
         "fleetwood mac": "tango in the night"}

pprint(music)
print("\n")
# Pretty-print the data structure

# Display details of one album recorded by a specific artist
print(music["jane taylor"])