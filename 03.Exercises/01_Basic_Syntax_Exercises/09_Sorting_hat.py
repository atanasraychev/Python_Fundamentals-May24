new_name = input()

while new_name != 'Welcome!':

    if new_name == 'Voldemort':
        print('You must not speak of that name!')
        break
    elif len(new_name) < 5:
        print(f'{new_name} goes to Gryffindor.')
    elif len(new_name) == 5:
        print(f'{new_name} goes to Slytherin.')
    elif len(new_name) == 6:
        print(f'{new_name} goes to Ravenclaw.')
    elif len(new_name) > 6:
        print(f'{new_name} goes to Hufflepuff.')
    new_name = input()

else:
    print('Welcome to Hogwarts.')
