import random
import sys

articles = ["a", "the", "another", "some"]
subjects = ["man", "dog", "woman", "cat", "platypus", "ferret"]
verbs = ["sang", "run", "played", "jumped",
         "prayed", "laughed", "danced", "pissed"]
adverbs = ["loudly", "quietly", "well", "badly"]


def compose(a, s, v, d):
    num = random.randint(0, 1)
    if (num == 1):
        print(a, s, v, d)
    else:
        print(a, s, v)


def say_poem(ls):
    count = 0
    while count < ls:
        art = random.choice(articles)
        sub = random.choice(subjects)
        ver = random.choice(verbs)
        adv = random.choice(adverbs)
        compose(art, sub, ver, adv)
        count += 1


while True:
    try:
        p = int(sys.argv[1])
        if (p in range(0, 11)):
            say_poem(p)
        else:
            print("usage: .\\awful_poetry2.py <number between 0 and 10>")
        break
    except IndexError:
        say_poem(5)
        break
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break
