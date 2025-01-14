# cook your dish here
t = int(input())

for _ in range(t):
    s = input() #hidden word
    g = input() #guess word
    m = ""
    
    for i in range(len(s)):
        if s[i] == g[i]:
            m += "G"
        else:
            m += "B"
    
    print(m)
