"""A simple Text Based Rock Paper Scissors Game."""

import random
import time

def rps():
    active = True
    while active:
        print("WELCOME to the game hope you will enjoy!")
        print("\n You have three Options 1.Rock\n 2.Paper\n 3.Scissors")
        print("Rules of the game is simple You have to choose any one of these: ")
        print("\nRock v/s Paper :- Rock Wins!\n Rock v/s Scissors :- Rock Wins\n Scissors v/s Paper :- Scissors Wins!")

        user_input = int(input("Enter your Choice: "))
        comp_choice = random.randint(1,3)
        time.sleep(5)

        def choice():
            print(f"User Input:- {user_input}")
            print(f"Computer Input:- {comp_choice}")

        if comp_choice == user_input:
            print("Computer is choosing another option")
            comp_choice = random.randint(1,3)
        
        if (user_input == 1 and comp_choice == 2):
            print(choice())
            print("Computer is the Winner")
            response = input("Do you want to try again ?")
            if response == "Yes" or response == "yes":
                print(rps())
            elif response == "No" or response == "no":
                print("Ok then Bye!")
                active = False
            else:
                print("Invalid!")
        elif (user_input == 1 and comp_choice == 3):
            print(choice())
            print("You are the winner")
            response = input("Do you want to play again?")
            if response == "Yes" or response == "yes":
                print(rps())
            elif response == "No" or response == "no":
                print("Ok then Bye!")
                active = False
            else:
                print("Invalid!")
        elif (user_input == 3 or comp_choice == 2):
            print(choice())
            print("You are the winner")
            response = input("Do you want to play again?")
            if response == "Yes" or response == "yes":
                print(rps())
            elif response == "No" or response == "no":
                print("Ok then Bye!")
                active = False
            else:
                print("Invalid!")
        elif (user_input == 2 and comp_choice == 1):
            print(choice())
            print("User is the Winner")
            response = input("Do you want to try again ?")
            if response == "Yes" or response == "yes":
                print(rps())
            elif response == "No" or response == "no":
                print("Ok then Bye!")
                active = False
            else:
                print("Invalid!")
        elif (user_input == 3 and comp_choice == 1):
            print(choice())
            print("Computer are the winner")
            response = input("Do you want to play again?")
            if response == "Yes" or response == "yes":
                print(rps())
            elif response == "No" or response == "no":
                print("Ok then Bye!")
                active = False
            else:
                print("Invalid!")
        elif (user_input == 2 or comp_choice == 3):
            print(choice())
            print("User is the winner")
            response = input("Do you want to play again?")
            if response == "Yes" or response == "yes":
                print(rps())
            elif response == "No" or response == "no":
                print("Ok then Bye!")
                active = False
            else:
                print("Invalid!")
rps()