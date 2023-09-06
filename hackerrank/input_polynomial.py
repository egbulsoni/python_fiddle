# Enter your code here. Read input from STDIN. Print output to STDOUT
xk = list(map(int, input().split(' ')))
x = xk[0]
k = xk[1]
p = input().replace('x', str(x))


def validate_polynomial(p, x, k):
    if eval(p) == k:
        return True
    return False


print(validate_polynomial(p, x, k))
