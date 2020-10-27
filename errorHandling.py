def div42(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")

print(div42(2))
print(div42(12))
print(div42(0))
print(div42(1))
