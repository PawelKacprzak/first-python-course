version = 3.7
print(version)
print(version > 3)
print(version <= 3)

number = 1200
print(number)
print(number > 1000)
print(number == 1200)
print(number == 1000)
print(number != 1200)
print(number != 1000)

if number > 1000:
    print('Higher than 1000')
else:
    print('Less than 1000')

age = 35
if age < 18:
    print('Unavailability')
else:
    print('Full access')

age = int(input('How old are you? '))
if age == 18:
    print('You are 18 years old')
elif age < 18:
    print('You are under 18 years old')
else:
    print('So... Probably you are old...')

