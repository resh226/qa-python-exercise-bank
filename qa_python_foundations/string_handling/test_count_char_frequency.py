# Function to count the frequency of each character in a string
def count_char_frequency(text):
    # Initialize an empty dictionary to store character counts
    freq = {}

    # Loop through each character in the input text
    for char in text:
        # If the character is already in the dictionary, increment its count
        if char in freq:
            freq[char] += 1
        # If the character is not in the dictionary, add it with count 1
        else:
            freq[char] = 1

    # Return the dictionary with character frequencies
    return freq

# Example usage
text = "banana"
result = count_char_frequency(text)

# Print the result
print(result)  # Output: {'b': 1, 'a': 3, 'n': 2}
