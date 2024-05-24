for i in '01234567896':
    i = int(i)
    if i == 6:
        print(i)
        break

print("#" * 10)

for i in '01234567896':
    i = int(i)
    if i == 6:
        print(i)

print("#" * 10)

for i in '01234567896':
    i = int(i)
    print(i)
    if i == 6:
        break

print("#" * 10)

sample = 'Python course'
for char in sample:
    if char == ' ':
        break
    print(char)

print("#" * 10)

for char in 'kowalskij@gmail.com':
    if char == '@':
        print('Valid email adress')
        break
else:
        print('Invalid email adress')