for i in range(10):
    if i == 6:
      continue
    print(i)

print('#' * 10)

for i in range(20):
    if i % 2 == 0:
      continue
    print(i)

print('#' * 10)

for i in range(20):
    if i % 2 == 1:
      continue
    print(i)

print('#' * 10)

sample = 'Python course'
for char in sample:
    if char == ' ':
      continue
    print(char)

print('#' * 10)

hashtags = '#summer#time#goodmood'
result = ''
for char in hashtags:
    if char == '#':
      print(result)
      result = ''
      continue
    result += char
print(result)
