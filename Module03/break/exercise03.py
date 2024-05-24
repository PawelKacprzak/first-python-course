panels = [
    {'id': 1, 'output_power': 200},
    {'id': 2, 'output_power': 150},
    {'id': 3, 'output_power': 250},
    {'id': 4, 'output_power': 100}
]

for panel in panels:
    if panel['output_power'] > 200:
        print('The first panel with an output power greater than 200 is: {}'.format(panel['id']))
        break
else:
        print('Any panel with an output power greater than 200.')
