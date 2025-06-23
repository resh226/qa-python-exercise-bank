def find_repeated_chars(word):
    # Dictionary to store character frequencies
    char_count = {}

    # List to store repeated characters and their counts
    repeated_chars = []

    # Loop through each character in the word
    for char in word:
        # If character already in dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        else:
            # If character not in dictionary, add it with count 1
            char_count[char] = 1

    #Loop through the dictionary to find characters with count >1.
    for char in char_count:
        count = char_count[char]
        if count > 1:
            #add the characters with count>1 as a list of tuples which stores va;ue like [(a,2),(b,4)]
            repeated_chars.append((char, count))

    return repeated_chars


# Take user input
word = input("Enter a word: ")

# Call the function and get the list of repeated characters
repeats = find_repeated_chars(word)

# Display results based on whether repeats were found
if repeats:
    print("Repeated characters:")
    #tuple unpacking, for each char present in the list of tuples,it fetches the char and the count
    for char, count in repeats:
        print(f"'{char}' appears {count} times")
else:
    print("No repeated characters found.")
