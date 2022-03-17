def show_homepage():
    print("     === DonateMe Homepage ===   ")
    print("--------------------------------------")
    print("| 1. Login       | 2. Register       |")
    print("--------------------------------------")
    print("| 3. Donate      | 4. Show Donations |")
    print("--------------------------------------")
    print("|           5. Exit                  |")
    print("--------------------------------------")


show_homepage()


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation = username, "donated", donation_amt
    print("Thank you for your donation!")
    return donation


def show_donations(donations):
    print("\n---All Donations---")
    if donations == 0:
        print("Currently, there are no donations.")
    else:
        print(donations)
