import getpass
import pickle

# database = {"nishant":"12345", "jatin":"45678"}
# pickle.dump( database, open( "save.txt", "wb" ) )
database = pickle.load ( open( "save.txt", "rb" ) )

while True:
    user_input = input("Sign in(S) or Register(R) ?\n")
    user_input = user_input.lower()
    if user_input == "s" or user_input == "r":
        break
    else:
        print("Please enter a valid character")
        continue


# For new users

if user_input == "r":
    while True:
        username = input("Create Your Username : ")
        if username in database.keys():
            print("Username already taken! \nPlease enter a different username")
            continue
        else:
            break
    password = input("Create your Password : ")
    # database.update({username:password})
    database[username]=password
    pickle.dump ( database, open( "save.txt", "wb" ) )
    print(database)
    while True:
        option = input("If you want to login now press L or press any character to quit\n")
        option = option.lower()
        if option == "l":
            break
        else:
            quit()


# For already registered users   

if user_input == "s" or option == "l":
    while True:
        username = input("Enter Your Username --> ")
        if username in database.keys():
            break
        else:
            print("Invalid username! \nPlease enter a valid username")
            continue
    while True:
        password = getpass.getpass("Enter Your Password --> ")
        if password == database[username]:
            print("Verified")
            break
        else:
            print("Invalid password! \nPlease enter a valid password")
            continue







    







