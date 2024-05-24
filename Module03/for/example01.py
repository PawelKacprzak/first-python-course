for i in 'python':
    print(i)

print('#' * 10)

for character in 'Paul':
    print(character)

print('#' * 10)

name = 'Rumpletilskinz'
index = 0

for char in name:
    print(index, char)
    index += 1

print('#' * 10)

for index in range(10):
    print(index)

print('#' * 10)

for index in range(len(name)):
    print('Index number: ', index, 'Character: ', name[index])

print('#' * 10)

for i in enumerate(name):
    print(i)

print('#' * 10)

for i, char in enumerate(name):
    print('Index number:', i, char)

print('#' * 10)

for i in [4, 5, 6, 8, 6]:
    print(i)

print('#' * 10)

for i, value in enumerate([4, 5, 6, 8, 6]):
    print(i, value)

print('#' * 10)

for i in range(10):
    print(i)

print('#' * 10)

for i in range(10, 20):
    print(i)

print('#' * 10)

for i in range(10, -1, -1):
    print(i)

print('#' * 10)

techs = 'java'
for i in range(len(techs)):
    print(i, techs[i])

print('#' * 10)

string = 'Python Course'
for char in string:
    print(char)

print()

for char in string[:6]:
    print(char)

print()

for char in string[::-1]:
    print(char)

print('#' * 10)

hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char not in '#':
        print(char)

print('#' * 10)

for char, number in zip('abcde', '12345'):
    print(char, number)

print('#' * 10)

result = ''

hashtags = '#sport#gym#fitness#'
for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        print(result)
        result = ''