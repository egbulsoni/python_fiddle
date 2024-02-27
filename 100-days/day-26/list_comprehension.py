names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
short_names = [name for name in names if len(name) <= 4]
long_names = [name for name in names if len(name) >= 5]
print(short_names)
print(long_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)

list_of_strings = input().split(',')
list_of_ints = [int(s) for s in list_of_strings]
result = [n for n in list_of_ints if n % 2 == 0]
print(result)

# sample input
# 9, 0, 32, 8, 2, 8, 64, 29, 42, 99

# sample output
# [0, 32, 8, 2, 8, 64, 42]