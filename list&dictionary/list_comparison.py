# Sample lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Check if lists are equal (same order and same elements)
if list1 == list2:
    print("list1 and list2 are equal")
else:
    print("list1 and list2 are not equal")

# Check if lists have same elements (ignoring order)
if sorted(list1) == sorted(list3):
    print("list1 and list3 have the same elements (unordered comparison)")
else:
    print("list1 and list3 are different")
