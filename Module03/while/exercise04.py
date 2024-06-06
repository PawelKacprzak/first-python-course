hour = 8
solar_power = 50
battery_capacity = 500
battery_level = 0

while hour < 15 or battery_level == battery_capacity:  
    hour += 1
    battery_level += solar_power
    print(f'Time: {hour}  \nBattery level: {battery_level} \n')
print(f'The solar battery charge level is: {battery_level} Watt-hours.')