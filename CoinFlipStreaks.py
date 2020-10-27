import random

numberOfStreaks = 0
streak = 0
CoinFlip = []

# Code that creates a list of 100 'heads' or 'tails' values.
for i in range(0,100):
    CoinFlip.append(random.randint(0,1))
# Code that checks if there is a streak of 6 heads or tails in a row.
for i in range(len(CoinFlip)):
    if i == 0:
        pass
    elif CoinFlip[i] == CoinFlip[i-1]: #check if current list item is same as before
        streak += 1
    else:
        streak = 0

    if streak == 6:
        numberOfStreaks += 1


print("Chance of streak: %s%%" % (numberOfStreaks / 100))












print('Chance of streak: %s%%' % (numberOfStreaks / 100))
