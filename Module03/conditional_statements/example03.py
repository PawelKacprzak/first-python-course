# balance = 10000
# customer_verification = True

# if balance > 0 and customer_verification:
#     print('You can withdraw cash.')
# else:
#     print('You can not withdraw cash.')

balance = 10000
customer_verification = True
amount = int(input('How much money you want to withdraw: '))

if balance > 0 and customer_verification and balance >= amount:
    print('You can withdraw cash.')
else:
    print('You can not withdraw cash. Insufficient amount: {}'.format(abs(balance - amount)))