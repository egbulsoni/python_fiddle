# Enter your code here. Read input from STDIN. Print output to STDOUT
amt = input()
ns = list(map(int, input().split(' ')))


def check_palint():
    fs = [n < 0 for n in ns]
    if (any(fs)):
        return False

    for n in ns:
        temp = [int(i) for i in str(n)]
        rev_temp = list(reversed(temp))
        # print(temp, 'rev_temp: ', rev_temp)
        t = ''.join(map(str, temp))
        r = ''.join(map(str, rev_temp))
        if (t == r):
            return True
    return False


print(check_palint())
