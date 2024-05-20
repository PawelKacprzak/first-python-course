print('Start program...')
print("""Hack the system buddy!
Two-digit PIN consists of digits: 0, 1, 2.""")

pin = input('Enter PIN: ')
if pin == '21':
    print('You crack the code!')
elif pin == '20':
    print('Whaaa... So close...')
else:
    print('Nope!')