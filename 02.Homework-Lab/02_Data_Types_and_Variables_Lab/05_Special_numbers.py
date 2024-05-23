number = int(input())

for check in range(1, number+1):
    digits_sum = 0

    first_digit = int(check / 10)
    second_digit = check % 10
    digits_sum = first_digit + second_digit

    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        print(f'{check} -> True')

    else:
        print(f'{check} -> False')
