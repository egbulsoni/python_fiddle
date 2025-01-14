#!/bin/python3

import math
import os
import random
import re
import sys
import operator


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=operator.itemgetter(k))

    for el in arr:
        s = ' '.join(str(x) for x in el)
        print(s)
