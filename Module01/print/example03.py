# interlude
hash = '#'

# account balance
balance = 40
balance += 30
print(f'Balance: {balance}')

balance = balance - 10
print('Balance: {}'.format(balance))
print(hash * 10)

# investment + accumulation factor + growth after one year
investment = 1000
accuFactor = 1 + 0.04
growthAfterOneYear = investment * accuFactor
print(f'Investment balance: {investment}')
print(f'Investment balance after one year: {growthAfterOneYear}')
print(hash * 10)