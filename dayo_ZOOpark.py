print("Welcome to online zoo ticket detail.")
age = "\nEnter you Age: "
age += "\nEnter 'quit' to exit.\n"

while True:
    age = input(age)
    if age.lower() == 'quit':
        print("\nPlease come back next time.")
        break
    
    age = int(age)
    if age < 3:
        print("\nThe Ticket is Free.")
        break
    elif age >= 3 and age <= 12:
        print("\nThe Ticket cost you 10$.")
        break
    else:
        print("\nThe Ticket cost you 15$.")
        break
print("\nThank you.")