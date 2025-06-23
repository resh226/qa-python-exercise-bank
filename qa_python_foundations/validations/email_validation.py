import re  # Import the regular expressions module for pattern matching


# Define a function to check if the given email is valid
def is_valid_email(email):
    # Universal regex pattern for email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # re.match() checks if the input matches the pattern from the beginning
    # bool() returns True if it's a match, otherwise False
    return bool(re.match(pattern, email))


# Ask the user to enter an email address
email = input("Enter your email address: ")

# Call the validation function and print the result
if is_valid_email(email):
    print("Valid email address.")  # If the function returns True
else:
    print("Invalid email address.")  # If the function returns False

