def main():
    name = input("What's your name? ")
    hello()
    # hello(name)


def hello(to="world"):
    print("hello,", to)


main()
