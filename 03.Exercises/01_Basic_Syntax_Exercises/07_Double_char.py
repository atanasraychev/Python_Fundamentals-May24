string_check = input()

while string_check != 'End':
    if string_check != "SoftUni":
        new_word = ''
        for char in string_check:
            new_word += 2 * char
        print(new_word)
    string_check = input()
