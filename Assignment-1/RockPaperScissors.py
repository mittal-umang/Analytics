# Chapter 5 Question 36
# (Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper
# game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
# wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
# scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
# 2 and displays a message indicating whether the user or the computer wins, loses,
# or draws.


import random


def __rockPaperScissor__(number):
    valueSet = {
        0: "Scissor",
        1: "Rock",
        2: "Paper"
    }

    return valueSet.get(number, "Invalid Number")


# function returns 1 for user and 0 for computer
# inputs num1 = input of user, num0 is input of computer
def __decider__(num1, num0):
    if num1 == 0 and num0 == 1:
        return 0
    elif num1 == 0 and num0 == 2:
        return 1
    elif num1 == 1 and num0 == 0:
        return 1
    elif num1 == 1 and num0 == 2:
        return 0
    elif num1 == 2 and num0 == 0:
        return 0
    elif num1 == 2 and num0 == 1:
        return 1
    else:
        pass


def main():
    cWins = 0
    uWins = 0
    while cWins < 2 and uWins < 2:
        num1 = eval(input("scissor (0), rock (1), paper (2): "))
        num0 = random.randint(0, 2)
        if num1 != num0 and num1 < 3:
            if __decider__(num1, num0) == 0:
                cWins += 1
                print("The computer is", __rockPaperScissor__(num0), ". You are ", __rockPaperScissor__(num1),
                      ".Computer Wins")
            elif __decider__(num1, num0) == 1:
                uWins += 1
                print("The computer is", __rockPaperScissor__(num0), ". You are ", __rockPaperScissor__(num1),
                      ".You Win")
        elif num1 > 2:
            print("Incorrect input.")
        else:
            print("The computer is", __rockPaperScissor__(num0), ". You are ", __rockPaperScissor__(num1),
                  ".Its a Draw")

    if cWins > uWins:
        print("Computer wins the game")
    elif uWins > cWins:
        print("You win the game")
    else:
        pass


if __name__ == "__main__":
    main()

