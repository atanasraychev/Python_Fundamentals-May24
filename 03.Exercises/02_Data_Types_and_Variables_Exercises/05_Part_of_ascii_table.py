first_char = int(input())
last_char = int(input())

for i in range(first_char, last_char):

    test = chr(i) # chr() converts a number to its related ASCII code symbol
    print(test, end=' ')
