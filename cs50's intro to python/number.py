def main():
    x = get_int("What's x?")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError as err:
            pass
            # print(err)
        # else:
            # return x
            # print(f"x is {x}")


main()
