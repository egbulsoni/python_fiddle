def main():
    yell("This", "is", "CS50")


def yell(*words):
    # uppercased = map(str.upper, words)
    # for word in words:
    #     uppercased.append(word.upper())
    # print(*uppercased)
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
