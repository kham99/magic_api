import pytest
import random



@pytest.fixture()
def generate_firstname():
    first_names = ['Oleg', 'Anna', 'Viktoriya', 'Alexander']
    return random.choice(first_names)

@pytest.fixture()
def generate_lastname():
    last_names = ['Smith', 'Johnson', 'Williams', "Petrov"]
    return random.choice(last_names)

@pytest.fixture()
def generate_totalprice():
    return random.randint(999, 99999)

@pytest.fixture()
def generate_additionalneeds():
    additionalneeds = ['Whore', 'suck my dick', 'viskey', 'orange', 'marihuanna', 'relax']
    return random.choice(additionalneeds)

