products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]

total = 0.0
discount = 0.0
items = 0

for product in products:
    total += product[1]
    items += 1

if items >= 2:
    discount = total - total * 0.1
    print('Total: {}\nAfter discount: {}'.format(total, discount))
else:
    print('Total: {}'.format(total))