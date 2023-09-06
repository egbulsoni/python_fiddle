# Enter your code here. Read input from STDIN. Print output to STDOUT
lines = list(map(int, input().split(' ')))
lists = []
flist = []
s = 0

for _ in range(lines[1]):
    ns = list(map(float, input().split(' ')))
    lists.append(ns)

rows = lines[1]
columns = lines[0]

avg_scores = list(zip(*lists))
for ss in avg_scores:
    print((sum(ss) / rows))
    # in case correcting to 1 decimal place is necessary (hackerrank specifies so)
    # print("{:.1f}".format((sum(ss) / rows)))
