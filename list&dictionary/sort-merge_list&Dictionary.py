# ---------- List Operations ----------

# Two sample lists
list1 = [4, 1, 7, 3]
list2 = [9, 2, 6]

# Sort a list
sorted_list1 = sorted(list1)
print("Sorted list1:", sorted_list1)

# Merge two lists
merged_list = list1 + list2
print("Merged list:", merged_list)

# Sort merged list
sorted_merged_list = sorted(merged_list)
print("Sorted merged list:", sorted_merged_list)

# ---------- Dictionary Operations ----------

# Two sample dictionaries
dict1 = {'c': 3, 'a': 1, 'b': 2}
dict2 = {'e': 5, 'd': 4}

# Merge two dictionaries (Python 3.9+ syntax)
merged_dict = dict1 | dict2
print("Merged dictionary:", merged_dict)

# Sort dictionary by keys
sorted_by_key = dict(sorted(merged_dict.items()))
print("Dictionary sorted by keys:", sorted_by_key)

# Sort dictionary by values
sorted_by_value = dict(sorted(merged_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by values:", sorted_by_value)
