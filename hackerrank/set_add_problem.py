# Enter your code here. Read input from STDIN. Print output to STDOUT
qt = int(input())


def country_stamps(qt):
    ls = set()
    for q in range(qt):
        ls.add(input())

    return len(ls)


print(country_stamps(qt))
