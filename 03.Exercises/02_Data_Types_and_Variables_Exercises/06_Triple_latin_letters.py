
number_of_letters = int(input())

for i in range(0, number_of_letters):
    for j in range(0, number_of_letters):
        for k in range(0, number_of_letters):

            print(f'{chr(97+i)}{chr(97+j)}{chr(97+k)}')
