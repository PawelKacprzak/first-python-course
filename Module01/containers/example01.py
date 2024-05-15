techs = {'python', 'java', 'c++', 'sql'}
print(techs)
print(type(techs))
print(len(techs))
print('#' *10)

if 'python' in techs:
    print('Yeah! I have the best programming language!')
print('#' *10)

print(set('python'))
print('#' *10)

techs.add('php')
print('Add new element in container techs:')
print(techs)
print('#' *10)

techs.remove('php')
print('Remove php from container techs:')
print(techs)
print('#' *10)

techs.pop()
print('Remove java from container techs:')
print(techs)
print('#' *10)

techs.clear()
print('Remove all elements from container techs:')
print(techs)
print('#' *10)