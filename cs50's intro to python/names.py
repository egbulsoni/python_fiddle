# names = []
# name = input("What's your name? ")

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())
# file.write(f"{name}\n")
# file.close()
# print(f"hello, {name}")

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

names = []
with open("names.txt") as file:
    for line in sorted(file):
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
