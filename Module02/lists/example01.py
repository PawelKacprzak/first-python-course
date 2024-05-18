empty_list = list()
print(empty_list)

techs = ['python', 'java', 'c++', 'go', 'sql']
techs[0] = 'python 3.7'
print(techs)

numbers = [3, 5, 3, 5, 23]
print(numbers)

mixed = ['python', 3.7, 4, True]
print(mixed)

empty = []
nested = [[1, 2, [3, 'sql']], ['python', 'java', 'go'], 3]
print(nested)

first_list = ['milk', 'potato', 'noodle']
second_list = ['water', 'eggs']
bucket = [first_list, second_list]
print(bucket)
print(len(bucket))

bucket = bucket + ['apples']
bucket += ['grapes']
print(bucket)