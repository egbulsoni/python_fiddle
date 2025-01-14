# Enter your code here. Read input from STDIN. Print output to STDOUT
# a = input()
# seta = input()
# n = input()
# print(f'a = {a}\nseta = {seta}\nn = {n}')
# for _ in range(int(n)):
#     try:
#         b = input()
#         c = input()
#         print(b)
#         print(c)
#     except EOFError as err:
#         print(err)
#     #     ns = input().split(' ')

na = int(input())
set_a = set(map(int, input().split(' ')))
nsets = int(input())

for _ in range(nsets):
    ns = input().split(' ')
    # print(ns)
    op = ns[0]
    set_b = set(map(int, input().split(' ')))
    if (op == 'update'):
        set_a |= set_b
    elif (op == 'intersection_update'):
        set_a &= set_b
    elif (op == 'difference_update'):
        set_a -= set_b
    elif (op == 'symmetric_difference_update'):
        set_a ^= set_b

print(sum(set_a))
