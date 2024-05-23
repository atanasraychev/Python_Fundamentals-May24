decorations_quantity = int(input())
days = int(input())

budget = 0
christmas_spirit = 0

for countdown in range(1, days+1):
    if countdown % 11 == 0:
        decorations_quantity += 2

    if countdown % 2 == 0:
        budget += 2 * decorations_quantity
        christmas_spirit += 5

    if countdown % 3 == 0:
        budget += 8 * decorations_quantity
        christmas_spirit += 13

    if countdown % 5 == 0:
        budget += 15 * decorations_quantity
        christmas_spirit += 17
        if countdown % 3 == 0:
            christmas_spirit += 30

    if countdown % 10 == 0:
        christmas_spirit -= 20
        budget += (5 + 3 + 15)

if days % 10 == 0:
    christmas_spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {christmas_spirit}')
