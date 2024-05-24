products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]
# total = 0
# j = 0

# for i in products:
#     test = products[j]
#     test = test[1]
#     total += test
#     j = j + 1

# print(total)

total = 0.0

for product in products:
    total += product[1]

print(total)