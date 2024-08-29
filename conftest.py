import pytest
import random


@pytest.fixture()
def send_book_id():
    return random.randint(1, 99)


@pytest.fixture()
def generate_username_swagger():
    username = ['kham99', 'amasnebes', 'karatel00']
    return random.choice(username)


@pytest.fixture()
def generate_password_swagger():
    password = ['asfdn3242', "hishnik32423", 'nasd3248sdhf32']
    return random.choice(password)


@pytest.fixture()
def generate_firstname():
    first_names = ['Oleg', 'Anna', 'Viktoriya', 'Alexander']
    return random.choice(first_names)


@pytest.fixture()
def generate_lastname():
    last_names = ['Smith', 'Johnson', 'Williams', "Petrov"]
    return random.choice(last_names)

@pytest.fixture()
def generate_email():
    email = ['Smith66@google.com', 'Karatel99@yandex.ru', 'vaevictis@outlook.com']
    return random.choice(email)

@pytest.fixture()
def generate_totalprice():
    return random.randint(999, 99999)


@pytest.fixture()
def checkin():
    checkin = ["2024-06-07", "2024-01-09", "2024-12-12"]
    return random.choice(checkin)


@pytest.fixture()
def checkout():
    checkout = ["2025-06-07", "2027-01-09", "2026-12-12"]
    return random.choice(checkout)


@pytest.fixture()
def generate_additionalneeds():
    additionalneeds = ['One', 'Hello World!', 'viskey', 'orange', 'Podgornaya', 'relax']
    return random.choice(additionalneeds)


@pytest.fixture()
def password_swagger():
    password = ["kham00", "amasnebes", "амир", "999000999", "&(*^%(fsnsd(*&^%^"]
    return random.choice(password)

@pytest.fixture()
def generate_phone():
    phone = ["899999999999", "79627677709", "89002223344", "99999999999", "89182247954"]
    return random.choice(phone)
