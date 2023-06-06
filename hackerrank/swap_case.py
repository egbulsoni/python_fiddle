def swap_case(s):
    chars = ""
    for c in s:
        if c.islower():
            chars += c.upper()
        elif c.isupper():
            chars += c.lower()
        else:
            chars += c
    return chars


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
