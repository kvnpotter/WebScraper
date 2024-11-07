import pytest

# Testing functions

def test_save():
    save({'Empty':'Dict'})
    assert os.path.exists('./results/leaders.json')
    with open('./results/leaders.json', 'r') as file:
              text = file.read()
              assert str(datetime.today().date()) == text[:10]