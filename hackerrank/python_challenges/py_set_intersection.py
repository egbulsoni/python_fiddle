a = input()
roll_a = list(map(int, input().split(' ')))
b = input()
roll_b = list(map(int, input().split(' ')))

print(len(set(roll_a).intersection(set(roll_b))))
