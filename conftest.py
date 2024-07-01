import pytest
import random


@pytest.fixture()
def send_book_id():
    return random.randint(1, 99)


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

@pytest.fixture()
def password_swagger():
    password = ["kham00", "amasnebes", "амирчиквсети", "999000999", "&(*^%(fsnsd(*&^%^"]
    return random.choice(password)
