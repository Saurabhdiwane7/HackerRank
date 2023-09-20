# Q = https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one


import math
import os
import random
import re
import sys


def plusMinus(arr):
    n = len(arr)
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for i in arr:
        if i > 0:
            positive_count += 1
        elif i < 0:
            negative_count += 1
        else:
            zero_count += 1

    positive_ratio = positive_count / n
    negative_ratio = negative_count / n
    zero_ratio = zero_count / n

    print(positive_ratio)
    print(negative_ratio)
    print(zero_ratio)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)