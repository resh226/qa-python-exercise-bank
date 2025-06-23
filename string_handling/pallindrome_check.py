# Function to check if the given input is a palindrome
def findpallindrome(user_input):
    # Initialize an empty string to hold the reversed version
    reversed_text = ""
    # Loop through each character in the input string
    for char in user_input:
        # Prepend the character to build the reversed string
        reversed_text = char + reversed_text

    # Compare the reversed and original text in uppercase to ignore case sensitivity
    if reversed_text.upper() == user_input.upper():
        return True
    else:
        return False

# Take input from the user
user_input = input("Enter the text: ")

# Call the function and store the result
result = findpallindrome(user_input)

# Print the result based on the returned value
if result:
    print(f"The text '{user_input}' is a palindrome ")
else:
    print(f"The text '{user_input}' is not a palindrome ")
