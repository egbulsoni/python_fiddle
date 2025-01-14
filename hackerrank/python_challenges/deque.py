from collections import deque

      
n = int(input())
ls = deque()
for i in range(n):
    op = input().split(' ')
    if(op[0] == "pop"):
        ls.pop()
    elif(op[0] == "popleft"):
        ls.popleft()
    if(op[0] == "append"):
        ls.append(op[1])
    elif(op[0] == "appendleft"):
        ls.appendleft(op[1])

ls = list(map(int, ls))
for n in ls:
    print(n, end=" ")