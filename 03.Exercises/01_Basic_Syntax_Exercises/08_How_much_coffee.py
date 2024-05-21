event = input()
coffee_count = 0

while event != 'END':
    if event.lower() == "coding" or \
            event.lower() == 'dog' or \
            event.lower() == 'cat' or \
            event.lower() == 'movie':
        if event.islower():
            coffee_count += 1
        else:
            coffee_count += 2
    event = input()

if coffee_count <= 5:
    print(coffee_count)
else:
    print("You need extra sleep")
