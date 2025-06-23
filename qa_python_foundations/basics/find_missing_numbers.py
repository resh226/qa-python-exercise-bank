def find_missing_numbers(numbers, N):
    #emply list
    missing = []
    #range(1, N+1) checks numbers from 1 to N (it excludes N +1)
    for i in range(1, N + 1):
        if i not in numbers:  # List check
            missing.append(i)
    return missing

# Step 1: Get value of N
N = int(input("Enter the value of N: "))

# Step 2: Get the list of numbers from user input
input_str = input("Enter the numbers (space-separated, some missing from 1 to N): ")
numbers = list(map(int, input_str.split()))

# Step 3: Find and display missing numbers
missing = find_missing_numbers(numbers, N)
print(f"Missing numbers from 1 to {N}: {missing}")
