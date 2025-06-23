


#if the input is number , convert it into string using str(0 and implement same logic.
def first_and_last_match(text):
    # string is like a array so zeroth index holds first value
    #Negative indexing allows you to access elements from the end.
    #-1 is the last character, -2 is second-last, and so on.
     if text[0] == text[-1]:
         return True
     else:
         return False


user_input = input("Enter a text: ")
if first_and_last_match(user_input):
    print(f"The first and last letter of {user_input} match")
else:
    print(f"The first and last letter of {user_input} do not match")