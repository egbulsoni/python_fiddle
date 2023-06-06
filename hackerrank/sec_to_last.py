import operator

if __name__ == '__main__':
    arr = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
    
    x = sorted(arr, key=operator.itemgetter(1))
    c = x[-1][1]
    x = sorted(arr, key=operator.itemgetter(0))
    
    for l,s in x:
        if s == c:
            print(l)
