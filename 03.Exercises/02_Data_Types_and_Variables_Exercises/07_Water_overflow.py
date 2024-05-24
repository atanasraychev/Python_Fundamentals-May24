number_of_water_flows = int(input())

tank_capacity = 255
water_quantity = 0
i = 0

while i <= number_of_water_flows:

    liters = int(input())
    if tank_capacity > water_quantity:
        water_quantity += liters
        print(water_quantity)
    else:
        print('Insufficient capacity!')

    i += 1

print(water_quantity)




