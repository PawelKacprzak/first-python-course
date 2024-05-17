string = 'Programowanie w języku Python - od A do Z'

string = string.lower()
# string = string.replace('-', '')
# string = string.replace(' ', '')
# string = string.replace('ę', 'e')
string = string.lower().replace('-', '').replace(' ', '').replace('e', 'ę')
# string = set(string)
string = len(set(string))

print(string)