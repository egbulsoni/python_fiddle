# Enter your code here. Read input from STDIN. Print output to STDOUT
shoe_quantity = int(input())
shoe_sizes = list(map(int, input().split(' ')))
shoe_stock = {}
customers = int(input())
amount_earned = 0

for shoe in shoe_sizes:
    if (shoe not in shoe_stock):
        shoe_stock[shoe] = 1
    else:
        shoe_stock[shoe] += 1

for i in range(customers):
    purchase_order = list(map(int, input().split(' ')))
    size, money_spent = purchase_order
    try:
        if shoe_stock[size] > 0:
            shoe_stock[size] -= 1
            amount_earned += money_spent
    except KeyError:
        continue
        # print(f"Size {size} not available, so no purchase.")

print(amount_earned)
