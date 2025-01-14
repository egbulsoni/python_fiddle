n = int(input())
s = set(map(int, input().split(' ')))
count = int(input())


def op_set():
    try:
        cmd = input().split(' ')
        try:
            j = int(cmd[1])
        except IndexError as err:
            # print(err)
            pass
        if (cmd[0] == 'pop'):
            s.pop()
        elif (cmd[0] == 'remove'):
            s.remove(j)
            return None
        elif (cmd[0] == 'discard'):
            s.discard(j)
            return None
    except KeyError as err:
        print("KeyError: ", err)

        return s


def sum_all():
    sum = 0
    for i in s:
        sum += i
    return sum


for _ in range(count):
    op_set()

print(sum_all())
