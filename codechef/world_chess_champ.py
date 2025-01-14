# cook your dish here
t = int(input())

for _ in range(t):
    prize = int(input())
    results = input()
    carl_points = 0
    chief_points = 0
    
    for c in results:
        if c == "C":
            carl_points += 2
        elif c == "D":
            carl_points += 1
            chief_points += 1
        elif c == "N":
            chief_points += 2
            
    
    if carl_points > chief_points:
        print(60 * prize)
    elif carl_points == chief_points:
        print(55 * prize)
    else:
        print(40 * prize)
        