# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())  # number of students English paper
roll_a = list(map(int, input().split(' ')))
b = int(input())
roll_b = list(map(int, input().split(' ')))

roll_ab = set(roll_a + roll_b)
print(len(roll_ab))
