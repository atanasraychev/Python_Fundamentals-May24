word = input()

reversed_word = ''
# creates empty string variable

# starts checking from the last letter.
# index start from 0, therefore a 5 letter word will have index 4 for last letter
# if we use len function - the script will place an error because there is nothing on index 5 position
# therefore we should start from index = string length-1

for i in range(len(word)-1, -1, -1):
    reversed_word += word[i]

print(reversed_word)