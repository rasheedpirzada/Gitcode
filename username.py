usernames = ['jamilmemon', 'ibteehajkazmi', 'adil_pirzada', 'rasheed_pirzada', 'ahsanawan']
new_users = input("Enter new username:\n")
while new_users:
    if new_users.lower() in usernames:
        print(new_users.lower() + " is already in use.")
        print("Please try new username.")
        break
    else:
        print(new_users.lower() + " is available.")
        break