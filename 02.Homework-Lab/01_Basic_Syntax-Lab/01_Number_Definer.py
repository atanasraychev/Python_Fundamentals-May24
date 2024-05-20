number = float(input())

if number == 0:
    # checks if number is 0
    print('zero')

elif number > 0:
    # checks all the positive number options
    if number < 1:
        print('small positive')
    elif number > 1000000:
        print('large positive')
    else:
        print('positive')

else:
    # checks all the negative number options
    if abs(number) < 1:
        print('small negative')
    elif abs(number) > 1000000:
        print('large negative')
    else:
        print('negative')
