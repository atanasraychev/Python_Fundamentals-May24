orders_count = int(input())

total_orders_price = 0.00

for orders in range(orders_count):

    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100.0:
        continue
    elif days not in range(1, 31+1):
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    single_order_price = capsule_price * days * capsules_per_day
    print(f'The price for the coffee is: ${single_order_price:.2f}')

    total_orders_price += single_order_price

print(f'Total: ${total_orders_price:.2f}')
