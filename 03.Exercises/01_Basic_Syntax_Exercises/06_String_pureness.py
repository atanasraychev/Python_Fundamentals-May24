number_of_strings = int(input())

for count in range(number_of_strings):

    test_string = input()

    for test_char in test_string:
        if test_char == ',' or test_char == '.' or test_char == '_':
            print(f"{test_string} is not pure!")
            break
    else:
        print(f"{test_string} is pure.")
