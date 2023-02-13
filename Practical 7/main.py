def is_palindrome(string):
    # Reverse the string using slicing
    reversed_string = string[::-1]
    print(reversed_string)
    # Check if the original string and the reversed string are equal
    for i in range(len(string)):
        if string[i] != reversed_string[i]:
            return False
    return True

# Get the string from the user
user_input = input("Enter a string: ")

# Check if the string is a palindrome and print the result
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
