import random

print(f"\nWelcome to Rock, Paper, Scissors!\n")

def player_turn():
    while True:
        user_choice = input("Choose R for Rock, P for Paper, S for Scissors!\n")
        valid_strings = ["r", "p", "s"]
        if user_choice in valid_strings:
            if user_choice == "s":
                print(f"You chose Scissors")
            elif user_choice == "p":
                print(f"You chose Paper")
            elif user_choice == "r":
                print(f"You chose Rock")
            return user_choice

        else:
            print(f"Invalid Input. Please choose r, p, or s.")

def computer_turn():
    comp_decision = random.choice(["r", "p", "s"])
    if comp_decision == "s":
        print(f"Computer chose Scissors\n")
    elif comp_decision == "p":
        print(f"Computer chose Paper\n")
    elif comp_decision == "r":
        print(f"Computer chose Rock\n")
    return comp_decision

def determine_winner():
    user_pick = player_turn()
    comp_pick = computer_turn()

    if user_pick == comp_pick:
        print(f"It was a tie!")
    elif user_pick == "s" and comp_pick == "p" or user_pick == "p" and comp_pick == "r" or user_pick == "r" and comp_pick == "s":
        print(f"You have won the game!")
    else: print(f"You have lost. The computer won!")
def main():
    while True:
        determine_winner()
        choice = input(f"\nWould you like to play again? y/n\n")
        if choice == "n":
            break

main()








