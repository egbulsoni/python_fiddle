import random

articles = ["a", "the", "another", "some"]
subjects = ["man", "dog", "woman", "cat", "platypus", "ferret"]
verbs = ["sang", "run", "played", "jumped",
         "prayed", "laughed", "danced", "pissed"]
adverbs = ["loudly", "quietly", "well", "badly"]
count = 0


def compose(a, s, v, d):
    num = random.randint(0, 1)
    if (num == 1):
        print(a, s, v, d)
    else:
        print(a, s, v)


while count < 5:
    art = random.choice(articles)
    sub = random.choice(subjects)
    ver = random.choice(verbs)
    adv = random.choice(adverbs)
    compose(art, sub, ver, adv)
    count += 1
