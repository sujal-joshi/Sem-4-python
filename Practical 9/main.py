print("Rock Paper Scissor Game")
print("Player 1 Make Your Move. R for Rock, S for Scissor and P for Paper: ")
player1 = input()
player1.lower()
print("Player 2 Make Your Move. R for Rock, S for Scissor and P for Paper: ")
player2 = input()

while True:
    if player1 == player2:
        print("It is a tie!")
    elif player1 == "r" and player2 == "s":
        print("Player 1 Wins!")
    elif player1 == "p" and player2 == "r":
        print("Player 1 Wins!")
    elif player1 == "s" and player2 == "p":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins")
    print("Thankyou for playing")
    play_again = input("Do you want to play again? y/n: ")
    if play_again != "y":
        break