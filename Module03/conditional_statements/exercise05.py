category = 'electronics'
price = 2000

if price > 1000 and category == 'electronics':
    price = price * 0.23
    print(f'The VAT for product is {price} $.')
elif price < 1000 and category == 'electronics':
    price = price * 0.08
    print(f'The VAT for product is {price} $.')
elif category == 'clothing':
    price = price * 0.23
    print(f'The VAT for product is {price} $.')
else:
    proce = price * 0.21
    print(f'The VAT for product is {price} $.')
