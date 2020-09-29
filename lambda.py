# A list of dictionaries
people = [
    {"name": "Tom", "house": "TP"},
    {"name": "Bill", "house": "OH"},
    {"name": "Brad", "house": "FL"},
    {"name": "Mike", "house": "MK"},
    {"name": "Ben", "house": "CH"},
    {"name": "Keith", "house": "OL"},
]

people.sort(key=lambda person: person["name"])

print(people)