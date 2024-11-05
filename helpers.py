import requests
import random
import string
from data.URL import Url

def generation_new_data_user():
    letters = string.ascii_lowercase
    email_new = f"{''.join(random.choice(letters) for i in range(7))}@yandex.ru"
    password_new = ''.join(random.choice(letters) for i in range(10))
    first_name_new = ''.join(random.choice(letters) for i in range(10))

    return {"email": email_new, "password": password_new, "name": first_name_new}


def generation_new_data_user_and_avtorization():
    user_data = generation_new_data_user()
    email = user_data["email"]
    password = user_data["password"]
    name = user_data["name"]

    payload = {
        "email": email,
        "password": password,
        "name": name,
    }

    # Create the new user
    response = requests.post(f"{Url.CREATE_USER}", data=payload)

    if response.status_code == 200:
        return {
            "user_data": user_data,
            "token": response.json().get("accessToken"),
            "response": response
        }
    else:
        raise Exception("User creation failed")