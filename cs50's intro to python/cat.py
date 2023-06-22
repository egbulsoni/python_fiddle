# i = 0
# while i < 3:
#     print("meow")
#     i += 1


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    # for _ in range(n):
    #     print("meow")
    print("meow\n" * n, end="")


i = get_number()
meow(i)
