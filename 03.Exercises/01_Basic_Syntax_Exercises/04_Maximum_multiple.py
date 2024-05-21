divider = int(input())

start_number = int(input())

for num in range(start_number,0,-1):
    if num % divider != 0:
        continue
    else:
        print (num)
        break
