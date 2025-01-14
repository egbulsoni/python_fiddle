def print_formatted(number):
    # your code goes here
    padding = len(str(format(number, "b")))
    for n in range(number):
        # converted number
        n_dec = n + 1
        n_octal = format(n_dec, "o")
        n_hexa = format(n_dec, "x").upper()
        n_binary = format(n_dec, "b")
        print(str(n_dec).rjust(padding, " "), end="")
        print(str(n_octal).rjust(padding + 1, " "), end="")
        print(str(n_hexa).rjust(padding + 1, " "), end="")
        print(str(n_binary).rjust(padding + 1, " "))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
