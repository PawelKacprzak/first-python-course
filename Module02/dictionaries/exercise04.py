fruits = {'apple': 2, 'banana': 3}
print('Dictionary before update:', fruits)

fruits.update({'apple': 4})
print('Dictionary after update:', fruits)

fruits['kiwi'] = 1
print('Dictionary after adding:', fruits)

# more_fruits = {'orange': 3, 'peach': 2}
# fruits = fruits | more_fruits
fruits.update({'orange': 3, 'peach': 2})
print('Dictionary after merging:', fruits)