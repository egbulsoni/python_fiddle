def count_substring(string, sub_string):
    i = 0
    c = 0
    n = 0
    while (n != -1):
        n = string.find(sub_string, i)
        if n != -1:
            c += 1
        i += n + 1
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
