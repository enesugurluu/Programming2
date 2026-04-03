import random

def start_computer():

    computer_choice_as_a_number = random.randint(1,3)
    if computer_choice_as_a_number == 1:
        computer_choice = "Rock"
    elif computer_choice_as_a_number == 2:
        computer_choice = "Paper"
    else:
        computer_choice = "Scissors"

    return computer_choice

def enter_user_choice():
    entered_choice = input("enter your choice: ")
    if entered_choice != "Rock" and entered_choice != "Paper" and entered_choice != "Scissors":
        print("Please enter 'Rock' or 'Paper' or 'Scissors'")
    return entered_choice

def main():
    computer_choice = start_computer()
    entered_choice = enter_user_choice()

    if entered_choice == computer_choice:
        print("Draw!")
    elif entered_choice == "Rock" and computer_choice == "Scissors":
        print("You win!, computer chose Scissors")
    elif entered_choice == "Paper" and computer_choice == "Rock":
        print("You win!, computer chose Rock")
    elif entered_choice == "Scissors" and computer_choice == "Paper":
        print("You win!, computer chose Paper")
    else:
        print(f"You lose!, computer chose {computer_choice}")


main()
