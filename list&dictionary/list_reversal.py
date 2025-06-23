# Original list
my_list = [10, 20, 30, 40, 50]

# Method 1: Using slicing
reversed_list = my_list[::-1]
print("Reversed list (using slicing):", reversed_list)

# Method 2: Using the built-in reverse() method (in-place)
my_list.reverse()
print("Reversed list (using reverse()):", my_list)

# Method 3: Using the reversed() function
my_list = [10, 20, 30, 40, 50]  # reset original list
reversed_list_2 = list(reversed(my_list))
print("Reversed list (using reversed()):", reversed_list_2)
