import config
import json


def login(username, password):
    login_data = {}
    with open('logins.json', 'r') as file:
        login_data = json.load(file)

    username_exists = False
    for x in login_data['user_data']:
        if x['username'] == username:
            username_exists = True

    if username_exists:
        for x in login_data['user_data']:
            if x['username'] != username:
                continue
            else:
                if x['password'] != password:
                    raise InvalidCredentialsError()
                else:
                    return
    else:
        print("username not found")
        raise UserDoesNotExistError()


class InvalidCredentialsError(Exception):
    pass


class UserDoesNotExistError(Exception):
    pass
