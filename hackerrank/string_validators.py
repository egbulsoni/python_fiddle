if __name__ == '__main__':
    s = input()
    a = [i.isalnum() for i in s]
    b = [i.isalpha() for i in s]
    c = [i.isdigit() for i in s]
    d = [i.islower() for i in s]
    e = [i.isupper() for i in s]
    print(any(a))
    print(any(b))
    print(any(c))
    print(any(d))
    print(any(e))

# credits to "rishabhg19"
# this solution is pure genious and I'd not be able to get this alone
