print("The zoo ticketing service")
prompt = "Enter your age: "
prompt += "\nEnter 'quit' to close"
while True:
    age = input(prompt)
    if age == 'quit':
        print("Thanks You.")
        break
    age = int(age)
    if age <= 5:
        print("The Ticket cost 10$.")
    elif age <= 16 and age > 5:
        print("The Ticket cost is 20$.")
    else:
        print("The Ticket cost is 30$.")

 