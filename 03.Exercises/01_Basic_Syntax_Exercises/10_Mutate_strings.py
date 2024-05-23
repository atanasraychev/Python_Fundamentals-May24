
first_word = input()
second_word = input()
letters = len(first_word)

for i in range(letters):

    test_word = first_word # creating the temporary word for testing if unique

    # extracting the first caracters from the second word from the start to position i+1 for each itteration
    char = second_word[0:i+1]

    # extracting the caracters from the first word from the i+1 position until the end for each itteration
    first_word = first_word[i+1:letters]

    # concat / merge both strings
    first_word = char + first_word

    # testing if newly created word is unique, different from the previously created
    if test_word == first_word:
        continue
    print(first_word)
