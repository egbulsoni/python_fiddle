# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
roll_a = list(map(int, input().split(' ')))
b = int(input())
roll_b = list(map(int, input().split(' ')))

print(len(set(roll_a) - set(roll_b)))
