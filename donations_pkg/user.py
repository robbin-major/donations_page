def login(database, username, password):
    if username in database and password == database[username]:
        print("Welcome", username, "!")
        return username
    if username in database and password != database[password]:
        print("Login Credintials Failed")
        return ""
    else:
        print("User not found. Please Register.")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered.")
        return ""
    else:
        print(username, "has been registered!")
        return username
