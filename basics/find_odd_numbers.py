#This program finds and returns odd numbers from the sample list

def find_odd_numbers(sample_list):
    odd_number_list = []  # Create an empty list
    for number in sample_list: # Loop through each number
        if number%2 != 0: # Check if the number is odd
            odd_number_list.append(number) # Add it to the list
    return odd_number_list # Return the final list

#sample list
sample_list= [3,4,5,6,23,34,56]
odd_numbers = find_odd_numbers(sample_list)
print(f"The list of odd numbers: {odd_numbers}") # return the list from function