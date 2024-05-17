list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

print('List with duplicates:', list1)
list2 = set(list1)
list2 = list2.union()
list2 = list(list2)
print('List without duplicate:', list2)