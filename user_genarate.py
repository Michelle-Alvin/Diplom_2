import random
import string

import requests


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_json_body_new_user():
    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload


def register_new_user_and_return_email_password():
    payload = generate_json_body_new_user()
    email_pass = {}

    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)

    if response.status_code == 200:
        email_pass = payload

    return email_pass
