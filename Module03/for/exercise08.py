rooms = [
    {
        'number': 101,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
        ],
    },
    {
        'number': 102,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
        ],
    },
    {
        'number': 103,
        'available_dates': [
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
    {
        'number': 105,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
    {
        'number': 107,
        'available_dates': [
            '2023-05-11',
            '2023-05-12',
        ],
    },
    {
        'number': 110,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
]

# for room in rooms:
#     if room['available_dates'][1] == '2023-05-10' or '2023-05-11' and room['available_dates'][-1] == '2023-05-13':
#         print('Available room: {}'.format(room['number']))

start_date = '2023-05-11'
end_date = '2023-05-13'

for room in rooms:
    if (
        start_date not in room['available_dates']
        or end_date not in room['available_dates']
    ):
        continue
    print(f"Room number {room['number']} is available.")