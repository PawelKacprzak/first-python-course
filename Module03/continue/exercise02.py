trainings = [
    {'name': 'Basic marksmanship', 'rank': 'Private'},
    {'name': 'Infantry tactics', 'rank': 'Corporal'},
    {'name': 'Art of war', 'rank': 'Sergeant'},
    {'name': 'Heavy weapons specialist', 'rank': 'Captain'},
    {'name': 'Advanced first aid', 'rank': 'Private'},
    {'name': 'Combat engineering', 'rank': 'Corporal'},
    {'name': 'Field intelligence', 'rank': 'Sergeant'},
    {'name': 'Military law', 'rank': 'Captain'},
    {'name': 'Parachuting', 'rank': 'Private'},
    {'name': 'Amphibious assault', 'rank': 'Corporal'},
    {'name': 'Counterterrorism', 'rank': 'Sergeant'},
    {'name': 'Military diplomacy', 'rank': 'Captain'},
]

for training in trainings:
    if training['rank'] != 'Sergeant':
        continue
    print(training['name'])