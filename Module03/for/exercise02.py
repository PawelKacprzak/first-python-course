hashtags = '#weekend#good#time#'
result = ''

for char in hashtags:
    if char != '#':
        result = result + char
    else:
        print(result)
        result = ''
