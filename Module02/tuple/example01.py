empty_tuple = tuple()
print(empty_tuple)

amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Google', 'USA', 'Technology', 2)

name_google = google[0]
print(name_google)

data = (amazon, google)
print(data)

user_details = ('Paul', 'Atreides')
print(user_details)

user_name = 'Paul'
user_surname = 'Atreides'
age = 'unknown'
user_more_details = user_name, user_surname, age
print(user_more_details)

user_name, surname, user_age = ('Paul', 'Atreides', 24)
print(user_name, surname, user_age)

amazon_name, country, sector, rank = amazon
print(amazon_name, country, sector, rank)

planets = 'Salus Secundus', 'Arrakis', 'Giede Prime'
print(planets)

nested = 'Europe', 'Poland', ('Warsaw', 'Krakow', 'Wroclaw')
print(nested)

x, y = 10, 15
x, y = y, x
print(x, y)