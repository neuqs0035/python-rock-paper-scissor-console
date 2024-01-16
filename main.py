from random import randint

class Game:
    @staticmethod
    def getComputerResponse() -> int:
        return randint(1, 3)

    @staticmethod
    def getChoiceName(choice: int) -> str:
        if choice == 1:
            return "Rock"
        elif choice == 2:
            return "Paper"
        elif choice == 3:
            return "Scissor"
        else:
            return "Invalid"

    @staticmethod
    def match(computer_response: int, user_input: int) -> bool:
        if user_input < 1 or user_input > 3:
            print("\nInvalid Input")
        elif user_input == 2 and computer_response == 1:
            return False
        elif user_input == 2 and computer_response == 3:
            return False
        elif user_input == 3 and computer_response == 1:
            return False
        elif user_input == computer_response:
            print("\nTie")
        else:
            return True

print("\n---------------------------------------")
print("\n|     Rock , Paper , Scissor Game     |")
print("\n---------------------------------------")

rps = Game()

while True:
    print("\nChoose Your Input\n\n1 Rock\n2 Paper\n3 Scissor")
    choice = int(input("\n_ : "))

    computer_choice = rps.getComputerResponse()
    print("\nYour Choice = " + rps.getChoiceName(choice))
    print("Computer Choice = " + rps.getChoiceName(computer_choice))

    if rps.match(computer_choice, choice):
        print("\nWOW, You Won!")
    else:
        print("\nComputer Wins")

    another_game = input("\nLet's Try Another Time (y/n) : ")

    if another_game.lower() == "y":
        continue
    else:
        print("\nPlay Another Time, See You Soon")
        break
