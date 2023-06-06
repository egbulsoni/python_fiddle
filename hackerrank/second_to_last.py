import operator

if __name__ == '__main__':
    arr = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
    
    x = sorted(arr, key=operator.itemgetter(1))
    for l, s in x:
        print(s)
    # c = x[1][1]
    # x = sorted(arr, key=operator.itemgetter(0))
    
    # for l,s in x:
    #     if s == c:
    #         print(l)

# 5
# Harsh
# 20
# Beria
# 20
# Varun
# 19
# Kakunami
# 19
# Vikas
# 21