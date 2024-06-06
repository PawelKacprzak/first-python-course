# PIN_CODE = '0000'
# user_pin = input('Please enter your PIN: ')

# while user_pin != PIN_CODE:
#     user_pin = input('Please try again: ')
# print('You are on board!')

print('#' * 10)

PIN_CODE = '0000'
user_pin = ''
counter = 0

while user_pin != PIN_CODE and counter < 3:
    user_pin = input('Please enter your PIN: ')
    if PIN_CODE == user_pin:
        print('You are on board!')
        break
    counter += 1
else:
    print('Login attempt limit exceeded...')
