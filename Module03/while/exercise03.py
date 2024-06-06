fuel = 100
fuel_consumption_rate = 10
time = 0

while fuel > 0:
    print('Fuel remaining: {} units.'.format(fuel))
    fuel -= fuel_consumption_rate
    time += 1
print('End of flight.')