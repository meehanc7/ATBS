import random

def collatz(number):
    if (number % 2) == 0:
        print(number // 2)
        return number // 2
    else:
        result = 3 * number + 1
        print(result)
        return result

try:
    r = input("Enter a number:\n>>> ")
    while r !=1:
        r = collatz(int(r))
except ValueError:
    print("Error! Please only enter integers.")
