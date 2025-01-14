# Enter your code here. Read input from STDIN. Print output to STDOUT
a_size = int(input())
a_lis = set(map(int, input().split()))
# if a_size != len(a_lis):
#     raise "error!"
b_size = int(input())
b_lis = set(map(int, input().split()))
# if a_size != len(a_lis):
#     raise "error!"
s = list()
s += a_lis.difference(b_lis)
s += b_lis.difference(a_lis)

s = sorted(s)

for v in s:
    print(v)
