import secure, rhodes, os, json

def start():

    print("Welcome to the Rhodes Login Screen! If you are an existing user, please type in 'existing-user' if you are a new user or 'new' \
if you are a new user!")

    value = '' # Value that represents whether user is new or existing

    while True: # Identifies whether user is new or existing
        command = input('Please enter your command here: ')
        if command == 'new':
            value = command
            break
        elif command == 'existing-user':
            value = command
            break

    if value == 'new': # What to do if the user is new
        un = ''
        pw = ''

        while True: # User is creating username
            user_t1 = input("Please enter your desired username: ")
            user_t2 = input("Please re-enter your username to confirm your choice: ")
            if user_t1 == user_t2: # If user typed same username twice
                un = user_t1
                break
            else: # If user failed to type same username twice
                print('You did not enter the same username twice, please try again!')

        while True: # User is creating password
            pw_1 = input("Please enter your desired password: ")
            pw_2 = input("Please re-enter your password to confirm your choice: ")
            if pw_1 == pw_2: # If user typed same password twice
                pw = pw_1
                break
            else: # If user failed to type same password twice
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

    else: # if the user is already on Rhodes

        print("Please enter your username and password")
        username = input("Username: ")
        password = input("Password: ")

        try: # Basic Security, EDIT LATER
            # Since this method returns, putting anything else will make it go to the except block
            secure.login(username, password)
        except:
            print("Invalid credentials!")
            quit()

        x = rhodes.Rhodes(username)
        x.run()

def add_user(user):
    """
    Helper function for start. When called, add_user() takes the input and appends it to the list of existing
    user data
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

    * When creating these files, create_files() will add an empty dictionary so these files are readable* 
    """
    folder_location = 'user_data/' + str(username)
    os.makedirs(folder_location) # Creates folder to store user data

    empty_json = {} # Empty variable needed in order to avoid read errors

    with open(os.path.join(folder_location, 'stocks.json'), 'w') as stks: # Creates stocks.txt for user
            json.dump(empty_json, stks)
    with open(os.path.join(folder_location, 'crypto.json'), 'w') as cryp: # Creates crypto.txt for user
        json.dump(empty_json, cryp)
    with open(os.path.join(folder_location, 'options.json'), 'w') as opt: # Creates options.txt for user
        json.dump(empty_json, opt)




if __name__ == "__main__":
    start()