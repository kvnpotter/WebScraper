# Imports

import json
from datetime import datetime

# Functions

def save(leaders_per_country: dict) -> None:
    '''
    Simple function to save passed dictionary to JSON file.
    '''
    now = str(datetime.today())
    leaders_per_country['DateTimeNow'] = now
    filename = input("Enter filename.json to create the file : ")
    with open(filename, "w") as output:
        output.write(json.dumps(leaders_per_country))
