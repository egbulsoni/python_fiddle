import math
print("Type integers, each followed by Enter; ^D or ^Z to finish")

total = []


def sort(ls):
    # implementação de bubble sort
    i = 0
    f = 1
    # ultima comparação
    lastcmp = len(ls)
    while (lastcmp != 1):
        while (f < lastcmp):
            if total[i] > total[f]:
                aux = total[i]
                total[i] = total[f]
                total[f] = aux
            f += 1
            i += 1
        # reinitialize variables
        lastcmp -= 1
        i = 0
        f = 1
    print(total)


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

sort(total)
if (len(total) % 2 == 1):
    c = int(math.ceil(len(total) / 2)) - 1
    print(c, "impar")
    print("median =", total[c])
else:
    c = int(math.ceil((len(total) / 2))) - 1
    d = int(math.floor((len(total) / 2)))
    m = (total[c] + total[d]) / 2
    print(c, d, "par")
    print("median =", m)
