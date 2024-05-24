lines_count = int(input())

total_sum = 0

for i in range(lines_count):
    # if lines_count > 20:
    #     break

    letter = input()
    total_sum += ord(letter) # ord() of a symbol gives the ASCII code of that symbol

print(f'The sum equals: {total_sum}')
