import textwrap

def wrap(string, max_width):
    s = ""
    i = 0
    for c in string:
        s += c
        i += 1
        if i % max_width == 0:
            s += "\n"
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)