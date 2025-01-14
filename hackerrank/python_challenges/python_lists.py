if __name__ == '__main__':
    N = int(input())
    ls = []
    for i in range(N):
        cmd = input().split(' ')
        c = cmd[0]
        # aliasing to numbers
        if (len(cmd) == 2 or len(cmd) == 3):
            n1 = int(cmd[1])
        if (len(cmd) == 3):
            n2 = int(cmd[2])

        # commands
        if c == "insert":
            ls.insert(n1, n2)
        elif c == "append":
            ls.append(n1)
        elif c == "print":
            print(ls)
        elif c == "sort":
            ls = sorted(ls)
        elif c == "remove":
            ls.remove(n1)
        elif c == "pop":
            ls.pop(-1)
        elif c == "reverse":
            ls.reverse()
