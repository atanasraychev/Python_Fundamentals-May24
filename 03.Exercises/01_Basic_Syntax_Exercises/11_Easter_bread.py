budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25

coloured_eggs = 0
breads = 0
used_budget = flour_price + eggs_price + 0.25 * milk_price

while budget > used_budget:

    breads += 1
    coloured_eggs += 3

    if breads % 3 == 0:
        coloured_eggs -= (breads - 2)

    budget -= used_budget
    used_budget = flour_price + eggs_price + 0.25 * milk_price

else:
    print(f'You made {breads} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.')
