import pytest
from SaveFunction import save

# Testing functions

@pytest.fixture
def setup_file():
       save({'Empty':'Dict'})

def test_save(setup_file):
    assert os.path.exists('./results/leaders.json')
    with open('./results/leaders.json', 'r') as file:
              text = file.read()
              assert str(datetime.today().date()) == text[:10]