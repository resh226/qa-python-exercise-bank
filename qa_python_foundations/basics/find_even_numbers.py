#This program finds and returns even numbers from the user input

#function to find and return even numbers
def find_even_numbers(user_input):
    #split() split the user input based on space an dmap function convert each number to in
    #list() convert it into list
    numberlist= list(map(int,user_input.split()))
    """list comprehension in Python.
    if num%2 meansif its even number
    for loop used for iteration of each number in the list
    list comprehension create a list by filtering or transforming items from another iterable (like a list)."""
    return [number for number in numberlist if number % 2==0 ]


#getting user input seperated by space so that it can be splitted based on space and conevrt to list format
user_input = input("Enter the list of numbers seperated by space:")
#call function
even_numbers= find_even_numbers(user_input)
#displaye the result by using the returned list from function
print(f"Even numbers are : {even_numbers}")