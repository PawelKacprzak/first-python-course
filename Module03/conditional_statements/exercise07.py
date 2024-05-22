category = 'crime'
quantity = 5
book_price = 100.0

if category == 'crime' and quantity >= 5:
    # boook_price -= book_price * 0.20
    book_price = book_price - book_price * 0.20
    print(f'The total price after the discount {book_price} $.')
elif category == 'crime' and quantity >= 3:
    book_price = book_price - book_price * 0.10
    print(f'The total price after the discount {book_price} $.')
elif category == 'crime' and quantity < 3:
    print(f'Price: {book_price} $.')
elif category == 'fantasy' and quantity >= 10:
    book_price = book_price - book_price * 0.25
    print(f'The total price after the discount {book_price} $.')
elif category == 'fantasy' and quantity >= 5:
    book_price = book_price - book_price * 0.15
    print(f'The total price after the discount {book_price} $.')
elif category == 'fantasy' and quantity < 5:
    print(f'Price: {book_price} $.')
elif category != 'fantasy' or category != 'crime' and quantity >= 20:
    book_price = book_price - book_price * 0.10
    print(f'The total price after the discount {book_price} $.')
elif category != 'fantasy' or category != 'crime' and quantity >= 10:
    book_price = book_price - book_price * 0.05
    print(f'The total price after the discount {book_price} $.')
elif category != 'fantasy' or category != 'crime' and quantity < 10:
    print(f'Price: {book_price} $.')
else:
    print('Error')
