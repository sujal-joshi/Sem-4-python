print("1 for Addition\n 2 for Subtraction\n 3 for Multiplication\n 4 for Division")
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
operation = int(input("Enter Operation: "))
if operation == 1:
    print(number1 + number2)
elif operation == 2:
    print(number1 - number2)
elif operation == 3:
    print(number1 * number2)
elif operation == 4:
    print(number1 / number2)
else:
    print("Invalid Operation")
