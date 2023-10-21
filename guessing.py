number = [37, 12, 55, 88, 19, 45, 23, 73, 96,]
prompt = "\nGuess any Number: "
prompt += "\nEnter 'Quit' to Exit: "

guess_active = True
while guess_active:
    guess = input(prompt)

    if guess.lower() == 'quit':
        guess_active = False
        break

    guess = int(guess)
    if guess <= 11:
        print("\nYou are little bit away from this.")
        print("Guess it! Guess it!")
    elif guess == 12:
        print("\nGreat! You are too good in guessing. Congratulations;).")
        repeat = input("\nWould you like to play again. \n(yes/no)\n")
        if repeat.lower() == 'no':
            break
    elif (guess >= 13) and (guess <= 18):
        print("\nThe Number you are Guessing is Right There.")
        print("Keep Trying and Thinking.")
    elif guess == 19:
        print("\nCongratulations! You are Intelligent Player.")
        repeat = input("\nWould you like to play again. \n(yes/no)\n")
        if repeat.lower() == 'no':
            break
    elif (guess >= 20) and (guess <= 22):   
        print("\nLittle bit Near.")
        print("just some steps away.")
    elif guess == 23:
        print("\nWOAHH! You Won.")
        repeat = input("\nWould you like to play again. \n(yes/no)\n")
        if repeat.lower() == 'no':
            break
    elif (guess >= 24) and (guess <= 44):
        print("\nRight Down There.")
        print("Keep Trying.")
    elif guess == 45:
        print("\nYEAH! YEAH! Right, YOU JUST WON.")
        repeat = input("\nWould you like to play again. \n(yes/no)\n")
        if repeat.lower() == 'no':
            break    
    elif (guess >= 46) and (guess <= 54):
        print("\nYou just little away from Winning..")
        print("Think to guess it correct.")
    elif guess == 55:
        print("\nHurrah! You Guess it right. Congratulations;).")
        repeat = input("\nWould you like to play again. \n(yes/no)\n")
        if repeat.lower() == 'no':
            break
    elif (guess >= 56) and (guess <= 72):
            print("\nTOO HIGH.")
            print("Think to guess it correct.")
    elif guess == 73:
        print("\nYou nailed it!")
        repeat = input("\nWould you like to play again. \n(yes/no)\n")
        if repeat.lower() == 'no':
            break
    elif (guess >= 74) and (guess <= 87):
        print("\nTOO LOW.")
        print("Think to guess it correct.")
    elif guess == 88:
        print("\nYahoo! Yippee! Hip hip hooray!")
        repeat = input("\nWould you like to play again. \n(yes/no)\n")
        if repeat.lower() == 'no':
            break
    elif (guess >= 89) and (guess <= 95):
        print("\njust right there, RIGHT THERE!.")
        print("Think and keep trying to guess it correct.")
    elif guess == 96:
        print("\nNICE, Time To Take a BOW!")
        repeat = input("\nWould you like to play again. \n(yes/no)\n")
        if repeat.lower() == 'no':
            break                    
    else:
        print("\nThe guessing Number isnt far away like there.")
        print("come back and keep trying.")

    

