# Imports

import json
from datetime import datetime

# Functions

def save(leaders_per_country: dict) -> None:
    '''
    Simple function to save passed dictionary to JSON file.
    '''
    now = str(datetime.today())
    filename = './results/leaders.json'
    with open(filename, "w") as output:
        output.write(now + "/n" + json.dumps(leaders_per_country))
