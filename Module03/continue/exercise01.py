missions = [
    {
        'name': 'Apollo 11',
        'date': '20.07.1969',
        'status': 'completed',
    },
    {
        'name': 'Mars Pathfinder',
        'date': '04.07.1997',
        'status': 'completed',
    },
    {
        'name': 'Chang\'e 4',
        'date': '03.01.2019',
        'status': 'in progress',
    },
    {
        'name': 'Cassini',
        'date': '15.10.1997',
        'status': 'completed',
    },
]

for mission in missions:
    if mission['status'] == 'in progress':
        continue
    print('Mission {} took place on {}'.format(mission['name'], mission['date']))