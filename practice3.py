import random

choices=["rock","paper","scissor"]

print("Choose Rock,Paper or Scissor")
#print("Type 'rock','paper,or'scissor' to play,'quit' with exit")

while True:

    user_choice=input("Enter your choice :").lower().strip()

    if user_choice == "quit":
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("please enter valid choice")
        continue

    computer_choice=random.choice(choices)
    print("Computer choice is :",computer_choice)

    if (user_choice == computer_choice):
        print("it's tie")

    elif (user_choice == "rock" and computer_choice == "scissor") or \
        (user_choice == "scissor" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    
    else:
        print("Computer Win")