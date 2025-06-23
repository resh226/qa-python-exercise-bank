
#An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
# using all original letters exactly once.
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase for case sensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted characters are the same
    return sorted(str1) == sorted(str2)

# Example usage
word1 = "Listen"
word2 = "Silent"

if is_anagram(word1, word2):
    print(f'"{word1}" and "{word2}" are anagrams.')
else:
    print(f'"{word1}" and "{word2}" are not anagrams.')