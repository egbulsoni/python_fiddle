fizz = "Fizz"
buzz = "Buzz"
for n in range(1,101):
    if n % 15 == 0:
        print(fizz + buzz)
        continue
    elif n % 3 == 0:
        print(fizz)
    elif n % 5 == 0:
        print(buzz)
    else:
        print(n)

    
