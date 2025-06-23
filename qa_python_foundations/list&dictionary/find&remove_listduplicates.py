# Original list with duplicates
my_list = [1, 2, 3, 2, 4, 5, 3, 6, 1]

# ---------- Method 1: Using set() to remove duplicates ----------
# This removes duplicates but does NOT preserve the original order
unique_list = list(set(my_list))
print("List after removing duplicates (unordered):", unique_list)

# ---------- Method 2: Remove duplicates while preserving order ----------
seen = []
for item in my_list:
    if item not in seen:
        seen.append(item)

print("List after removing duplicates (order preserved):", seen)

# ---------- Find and display duplicates only ----------
duplicates = []
for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Duplicate elements found:", duplicates)
