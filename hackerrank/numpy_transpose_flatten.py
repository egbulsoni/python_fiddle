# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

ns = input()
ns = ns.split()
my_array = []
for i in range(int(ns[0])):
    row = input()
    row = row.split()
    row = np.array([int(j) for j in row])
    if len(row) != int(ns[1]):
        raise Exception(f"you should've inserted {ns[1]} numbers per row!")
    my_array.append(row)

print(np.transpose(my_array))
out = np.concatenate(my_array).ravel()
print(out)

# print(type(out))