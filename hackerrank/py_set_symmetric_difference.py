# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
roll_a = set(list(map(int, input().split(' '))))
b = input()
roll_b = set(list(map(int, input().split(' '))))

print(len(roll_a.symmetric_difference(roll_b)))
