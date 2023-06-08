def apply_command(c, ls, n1=0, n2=0):
    if c == "insert":
        if (n1 > len(ls)):
            raise Exception("error, invalid index")
        ls.insert(n1, n2)
    elif c == "append":
        ls.append(n1)
    elif c == "print":
        print(ls)
    elif c == "sort":
        ls = sorted(ls)
    elif c == "remove":
        del (ls[n1])
    elif c == "pop":
        ls.pop(-1)
    elif c == "reverse":
        return ls.reverse()
    return ls


if __name__ == '__main__':
    N = int(input())
    ls = list()
    for i in range(N):
        cmd = input().split(' ')
        apply_command(str(cmd[0]), ls, int(cmd[1]), int(cmd[2]))
        print(ls)
