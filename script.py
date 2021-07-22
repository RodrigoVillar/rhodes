"""
Script that acts as a precursor to Rhodes

This script (script.py) is separated from the other Rhodes modules (rhodes.py, front_end.py, etc.) as it heavily relies on
functions while the other Rhodes modules are more object-oriented. When run, this script calls start(), which performs login
functions and eventually leads the user to the run() method of Rhodes. 

This method is at the bottom of the Rhodes call stack.
"""

import secure
import rhodes
import os
import json


def start():
    """
    Method that starts Rhodes. Once called, start() first sees if the user is new or already has a Rhodes account. If the user
    is new, start() calls add_user() and create_files() to add the new user to the list of existing user and to create the files necessary
    for the new user to use Rhodes, respectively. If the user already has an account, start() uses the secure module to see if their 
    credentials are valid in order to log them in. Regardless of user startus, start() then creates a Rhodes object (inserting data if the
    user already has an account) and calls run() for that object.
    """

    print("Welcome to the Rhodes Login Screen! If you are an existing user, please type in 'existing-user' if you are a new user or 'new' \
if you are a new user!")

    value = ''  # Value that represents whether user is new or existing

    while True:  # Identifies whether user is new or existing
        command = input('Please enter your command here: ')
        if command == 'new':
            value = command
            break
        elif command == 'existing-user':
            value = command
            break

    if value == 'new':  # What to do if the user is new
        un = ''
        pw = ''

        while True:  # User is creating username
            user_t1 = input("Please enter your desired username: ")
            user_t2 = input(
                "Please re-enter your username to confirm your choice: ")
            if user_t1 == user_t2:  # If user typed same username twice
                if unique_username(user_t1):
                    un = user_t1
                    break
                else:
                    print("Sorry, but that username is taken. Please try again!")
            else:  # If user failed to type same username twice
                print('You did not enter the same username twice, please try again!')

        while True:  # User is creating password
            pw_1 = input("Please enter your desired password: ")
            pw_2 = input(
                "Please re-enter your password to confirm your choice: ")
            if pw_1 == pw_2:  # If user typed same password twice
                pw = pw_1
                break
            else:  # If user failed to type same password twice
                print("You did not enter the same password twice, please try again!")

        new_data = {
            "username": un,
            "password": pw
        }

        add_user(new_data)
        create_files(un)

        x = rhodes.Rhodes()
        x.set_username(un)
        x.run()

    else:  # if the user is already on Rhodes

        print("Please enter your username and password")
        username = input("Username: ")
        password = input("Password: ")

        try:  # Basic Security, EDIT LATER
            # Since this method returns, putting anything else will make it go to the except block
            secure.login(username, password)
        except:
            print("Invalid credentials!")
            quit()

        x = rhodes.Rhodes(username)
        x.run()


def add_user(user):
    """
    Helper function to start()

    When called, add_user() will add the user's credentials to the system.

    Parameter user: the users credentials
    Precondition: user is a dictionary that contains the following keys: "username", "password"
    """
    login_file_json = {}

    with open('logins.json') as file:
        login_file_json = json.load(file)

    login_file_json['user_data'].append(user)

    with open('logins.json', 'w') as file:
        json.dump(login_file_json, file)


def create_files(username):
    """
    Helper function for start(). When called, create_files() will create a new directory
    based on the username given. It will then create the following files:

    crypto.json, options.json, stocks.json

    Parameter username: the username of the user
    Precondition: handled by script.py

    * When creating these files, create_files() will add an empty dictionary so these files are readable* 
    """
    folder_location = 'user_data/' + str(username)
    os.makedirs(folder_location)  # Creates folder to store user data

    empty_json = {}  # Empty variable needed in order to avoid read errors

    with open(os.path.join(folder_location, 'stocks.json'), 'w') as stks:  # Creates stocks.json for user
        json.dump(empty_json, stks)
    with open(os.path.join(folder_location, 'crypto.json'), 'w') as cryp:  # Creates crypto.json for user
        json.dump(empty_json, cryp)
    with open(os.path.join(folder_location, 'options.json'), 'w') as opt:  # Creates options.json for user
        json.dump(empty_json, opt)
    with open(os.path.join(folder_location, 'rhodes.json'), 'w') as rho:
        json.dump(empty_json, rho)


def unique_username(input):
    """
    Helper function to start()

    When called, unique_username() first grabs data from the json containing all login information. It then
    loops through each username with the condition: if any username matches input, it returns False. Otherwise, it returns True.

    Parameter input: the desired username of the user
    Precondition: none
    """
    with open("logins.json", "r") as file:
        logins = json.load(file)

    login_list = logins["user_data"]

    for x in login_list:
        if x["username"].lower() == input.lower():
            return False

    return True


if __name__ == "__main__":
    start()
