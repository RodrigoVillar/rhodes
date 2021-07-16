import secure, rhodes,pickle

def start():
    print("Please enter a username and password")
    username = input("Username: ")
    password = input("Password: ")

    try: # Basic Security, EDIT LATER
        secure.login(username, password)
    except:
        print("Invalid credentials!")
        quit()
    
    


if __name__ == "__main__":
    start()