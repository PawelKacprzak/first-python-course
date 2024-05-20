empty_dict = dict()
print(empty_dict)

new_empty_dict = {}
print(type(new_empty_dict))

# dict = {'key' : 'value'}

pol_to_eng = {
    'jeden' : 'one',
    'dwa' : 'two',
    'trzy' : 'three'
}
print(pol_to_eng)

name_to_digit = {
    'one' : 1,
    'two' : 2,
    'three' : 3
}
print(name_to_digit)
print(len(name_to_digit))

pol_to_eng['cztery'] = 'four'
print(pol_to_eng)

pol_to_eng_copied = pol_to_eng.copy()

pol_to_eng.clear()
print('After clear:', pol_to_eng)

print(pol_to_eng_copied.keys())
# list(pol_to_eng_copied.keys())
print(pol_to_eng_copied.values())
# list(pol_to_eng_copied.values())
print(pol_to_eng_copied.items())
# list(pol_to_eng_copied.items())

print(pol_to_eng_copied['jeden'])
# print(pol_to_eng_copied('pięć'))

print(pol_to_eng_copied.get('zero', 'NaN'))

pol_to_eng_copied.pop('dwa')
print(pol_to_eng_copied)

pol_to_eng_copied.popitem()
print(pol_to_eng_copied)

pol_to_eng_copied.update({'jeden' : 'eins'})
print(pol_to_eng_copied)