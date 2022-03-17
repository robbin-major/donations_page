from donations_pkg.homepage import show_homepage
from donations_pkg.user import login
from donations_pkg.user import register
from donations_pkg.homepage import donate
from donations_pkg.homepage import show_donations
database = {"admin": "password123"}
donations = []
authorized_user = ""
show_homepage()
if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print("Logged in as", authorized_user)


while True:
    show_homepage()
    user = input("Choose an option: ")
    if user == "1":
        username = input("Enter Username:")
        password = input("Enter Password:")
        authorized_user = login(database, username, password)

    elif user == "2":
        username = input("Enter Username:")
        password = input("Enter Password:")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
    elif user == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)

        user = input("Choose an option:")
    elif user == "4":
        show_donations(donations)
    elif user == "5":
        print("Goodbye!")
        break
