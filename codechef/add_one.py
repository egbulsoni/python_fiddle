# cook your dish here
t = int(input())
for _ in range(t):
    bign = input()
    li_bign = list(bign)
    carry_one = True
    for i in range(len(li_bign)-1, -1, -1):
        bn = int(li_bign[i])
        if bn == 9 and carry_one:
            li_bign[i] = "0"
            carry_one = True
        else:
            if carry_one:
                li_bign[i] = str(bn + 1)
                carry_one = False
        if carry_one and i == 0:
            li_bign = ['1'] + li_bign
        
    print(''.join(li_bign))