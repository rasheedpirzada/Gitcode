print("The zoo ticketing service")
prompt = "Enter your age: "
prompt += "\nEnter 'quit' to close:\n"
while True:
    age = input(prompt)
    if age == 'quit':
        print("Thanks You.")
        break
    age = int(age)
    if age <= 3:
        print("The Ticket cost 10$.")
    elif age <= 13 and age > 3:
        print("The Ticket cost is 20$.")
    else:
        print("The Ticket cost is 30$.")