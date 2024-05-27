raw_data = '345!23!3234!43434'
clean_data = ''

for num in raw_data:
    if num != '!':
        clean_data += num
    else:
        print(clean_data)
        clean_data = ''
print(clean_data)

print('#' * 10)

clean_data = ''
for num in raw_data:
    if num != '!':
        clean_data += num
    else:
        clean_data += ','
print(clean_data)

print('#' * 10)

raw_data = raw_data.replace('!', ',')
print(raw_data)

print('#' * 10)

balance = 450

print('Balance: {}'.format(balance))
for money in range(10, 60, 10):
    print('Withdraw: {}'.format(money))
    balance -= money
    print('Balance: {}'.format(balance), '\n')
print('Final balance: {}'.format(balance))

print('#' * 10)

code = '1234pp'

for char in code:
    if char.isnumeric():
        continue
    else:
        print('Youe code can contains only numbers')
        break

if code.isnumeric():
    print('Good code, you have full access')
else:
    print('Please improve your code')

print('Good code')

print('#' * 10)
print('\n' * 4)

print(' Welcome to the login system!')
print('*' * 30)
nick = input('Enter your nickname: ')
pin = input('Hi {}, please enter your PIN: '.format(nick))

if len(pin) == 4:
    for char in pin:
        if char not in '0123456789':
            print('Incorrect PIN! PIN can only contain digits.')
            break
    else:
        print('Correct PIN {}. You have logged into your account.'.format(nick))
else:
    print('Check that your pin has the right number of digits and contains only digits.')
print('')
