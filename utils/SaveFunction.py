# Imports

import json
from datetime import datetime
import pytest
import os

# Functions

def save(leaders_per_country: dict) -> None:
    '''
    Simple function to save passed dictionary to JSON file.
    '''
    now = str(datetime.today())
    filename = './results/leaders.json'
    with open(filename, "w") as output:
        output.write(now + "/n" + json.dumps(leaders_per_country))

# Testing functions

def test_save():
    save({'Empty':'Dict'})
    assert os.path.exists('./results/leaders.json')
    with open('./results/leaders.json', 'r') as file:
              text = file.read()
              assert str(datetime.today().date()) == text[:10]

if __name__ = "__main__":
    pytest.main(['-v'])