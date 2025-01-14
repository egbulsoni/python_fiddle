t = int(input())

def split_seq(seq):
    ls = []
    for i in range(2,len(seq)+1, 2):
        ls.append(seq[i-2:i])
        
    return ls

def return_protein(ns):
    if ns == "00":
        return 'A'
    elif ns == "01":
        return 'T'
    elif ns == "10":
        return "C"
    elif ns == "11":
        return "G"

while t > 0:
    n = int(input())
    s = input()
    # Your code goes here
    seq = split_seq(s)
    # print(seq)
    ps = "".join(list(map(return_protein, seq)))
    print(ps)
    t -= 1
    

