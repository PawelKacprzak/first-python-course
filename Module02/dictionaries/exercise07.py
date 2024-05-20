people = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}

# print(people.get('Emma', 20))
# people['Emma'] = 20
emma_age = people.setdefault('Emma', 20)
print(emma_age)
print(people)