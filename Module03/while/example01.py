i = 0

while i < 5:
    print(i)
    i = i + 1

print('#' * 10)

while True:
    print(i)
    if i >= 10:
        break
    i += 1

print('#' * 10)

# while True:
#     name = input('Name: ')
#     if len(name) >= 3 and name.isalpha():
#         break
# print('Hello {}!'.format(name))

print('#' * 10)

n = 0

while n < 20:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

print('#' * 10)

searching_list = [12, 53, 13, 63, 34]
flag = False
need_this = 44
idx = 0

# while idx < len(searching_list):
#     if searching_list[idx] == need_this:
#         flag = True
#         break
#     idx += 1
# if flag:
#     print('I found it: {}'.format(need_this))

while idx < len(searching_list):
    if searching_list[idx] == need_this:
        flag = True
        break
    idx += 1
if not flag:
    searching_list.append(need_this)
    print('I add it: {}'.format(need_this))
    print(searching_list)
    