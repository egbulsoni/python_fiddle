qtd = int(input())

for q in range(qtd):
    try:
        nums = list(map(int, input().split(' ')))
        div = nums[0] // nums[1]
        print(div)
    except ZeroDivisionError as err:
        print("Error Code:", err)
    except ValueError as err:
        print("Error Code:", err)
