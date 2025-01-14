import operator

if __name__ == '__main__':
    arr = list()
    scores = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])

    x = sorted(arr, key=operator.itemgetter(1))
    m = x[0][1]
    second_lowest = m

    for n, s in x:
        if s > second_lowest:
            second_lowest = s
            break

    x = sorted(arr, key=operator.itemgetter(0))

    for n, s in x:
        if s == second_lowest:
            print(n)
