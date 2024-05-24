products = [('T-shirt', 'Clothing',50.00), ('Pants', 'Clothing', 100.00), ('Shoes', 'Footwear', 150.00)]

for product in products:
    if product[1] == 'Clothing':
        print(product[0], product[2])