#!/usr/bin/python3
from random import randint


def highest_random(limit):
    highest = 0
    for i in range(5):
        r = randint(0, limit)
        if r > highest:
            highest = r

    msg = "Hello {num:d}".format(num=highest)
    return msg


def hello_world():
    upper_limit = 100
    msg = highest_random(upper_limit)
    return msg


if __name__ == '__main__':
    print(hello_world())
