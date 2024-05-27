words = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

max_balance = 50
balance = 0
new_dict = {}
i = 0

while balance < max_balance:
    for pldig, digs in words.items():
        if pldig not in new_dict:
            new_dict[pldig] = digs
        else:
            new_dict[pldig] += digs
        balance += digs
        # if balance >= max_balance:
        #     break
    i += 1

print('To build the number {} you need:'.format(max_balance))
for pldig, digs in new_dict.items():
    print(pldig.capitalize(), 'number in quantity',i,'that is in total', digs)