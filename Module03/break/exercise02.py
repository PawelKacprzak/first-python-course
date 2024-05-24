cars = [
    {'model': 'Tesla', 'mileage': 5000, 'battery_level': 100},
    {'model': 'BMW', 'mileage': 1500, 'battery_level': 80},
    {'model': 'Toyota', 'mileage': 15000, 'battery_level': 100},
    {'model': 'Mercedes', 'mileage': 5000, 'battery_level': 75}
]

for car in cars:
    if car['battery_level'] == 100:
        print(car['model'])
        break