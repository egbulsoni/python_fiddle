print("Type integers, each followed by Enter; ^D or ^Z to finish")

total = []

while True:
    try:
        line = input()
        if line:
            number = int(line)
            total.append(number)
        else:
            break
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break

if total:
    print("numbers =", total, "min =", min(total), "max=", max(total), "count =", len(total), "total =", sum(
        total), "mean =", sum(total) / len(total))
