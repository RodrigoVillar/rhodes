import secure, rhodes,pickle

def start():
    print("Please enter a username and password")
    username = input("Username: ")
    password = input("Password: ")

    try: # Basic Security, EDIT LATER
        # Since this method returns, putting anything else will make it go to the except block
        secure.login(username, password)
    except:
        print("Invalid credentials!")
        quit()
    
    # Until there is a way to save user data, an Rhodes object is instantiated everytime we run Rhodes
    x = rhodes.Rhodes("Rodrigo Villar", "07/16/2021")
    x.run()
    



if __name__ == "__main__":
    start()