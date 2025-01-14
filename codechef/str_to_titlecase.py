# cook your dish here
t = int(input())
for _ in range(t):
    s = input()
    pals = s.split(' ')
    fp = []
    for p in pals:
        if p.isupper():
            fp.append(p)
        else:
            fp.append(p.title())
    
    fp = " ".join(fp)
    print(fp)
            