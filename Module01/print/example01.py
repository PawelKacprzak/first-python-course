print('Hello again!')

info = 'Hello again!'
print(info)

print('Hello', end=' ')
print('again!')

print('Hello', 'again!', sep='^-^')

with open('file.txt', 'w') as f:
    print('Hello again!', file=f)
    print('I really love Python!', file=f)

print("""
      WOW!
      Hello
      again! 
      """)