proportions = {
    'flour': 500,
    'salt': 4,
    'sugar': 200,
    'butter': 150,
}

# amount_of_dough = 3000
# ingradients = list(proportions.items())
# total = 0
# i = 0
# a = 0

# while total < amount_of_dough:
#     total += ingradients[0][1]
#     total += ingradients[1][1]
#     total += ingradients[2][1]
#     total += ingradients[3][1]
#     i += 1
# print('To prepare {} g of dough, you need:'.format(amount_of_dough))

# for ingradient in ingradients:
#     print(ingradients[a][0].capitalize(), '-' ,ingradients[a][1] * i, 'g')
#     a += 1

amount_of_dough = 3000
counter = 0
ingredients = {}
 
while counter < amount_of_dough:
    for ingredient, amount in proportions.items():
        if ingredient not in ingredients:
            ingredients[ingredient] = amount
            # print(amount)
            # print(ingredient)
        else:
            ingredients[ingredient] += amount
        counter += amount
        # print(counter)
        # print(amount)

print('To prepare', amount_of_dough, 'g of dough, you need:')
for ingredient, amount in ingredients.items():
    print(ingredient.capitalize(), '-', amount, 'g')