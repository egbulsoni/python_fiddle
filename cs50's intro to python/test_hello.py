from hello3 import hello


def test_default(to="world"):
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"


if __name__ == "__main__":
    main()
