import random

while True:
    user_input = int(input("Enter a Random Number between 0 to 10: "))
    random_number = random.randint(1, 9)
    if user_input < 0:
        print("Please enter number between 0 and 10")
    elif user_input > 9:
        print("Please enter number between 0 and 10")
    elif user_input > random_number:
        print("You guessed too high, the number is ", random_number)
    elif user_input < random_number:
        print("You guessed too low, the number is ", random_number)
    elif user_input == random_number:
        print("Yayyyy! You guessed the exact number, the number is ", random_number)
    else:
        print("Invalid Operation")

    play_again = input("Do you want to play again? y/n ")
    if play_again != "y":
        break
