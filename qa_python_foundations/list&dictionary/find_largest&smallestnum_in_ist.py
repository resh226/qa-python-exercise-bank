# Sample list
my_list = [10, 25, 3, 87, 42, 1, 66]

# Method 1: Using built-in functions
largest = max(my_list)
smallest = min(my_list)

print("Largest number (using max):", largest)
print("Smallest number (using min):", smallest)

# Method 2: Using loop (manual way)
max_num = my_list[0]
min_num = my_list[0]

for num in my_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Largest number (using loop):", max_num)
print("Smallest number (using loop):", min_num)
