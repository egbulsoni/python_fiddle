# Enter your code here. Read input from STDIN. Print output to STDOUT
fl = list(map(int,input().split(' ')))
sl = list(map(int,input().split(' ')))
prod = list()

for i in fl:
    for j in sl:
        prod.append((i, j))
        
for p in prod:
    print(p, end=" ")