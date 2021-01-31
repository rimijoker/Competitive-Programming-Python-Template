import os
import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br


inp_int = lambda: int(input())
inp_string = lambda: input().strip()
inp_string_list = lambda: list(input().split())
inp_char_list = lambda: list(input().strip())
inp_int_map = lambda: map(int, input().strip().split())
inp_float_map = lambda: map(float, input().strip().split())
inp_int_list = lambda: list(map(int, input().strip().split()))

ceil = lambda x: int(x) if (x == int(x)) else int(x) + 1
ceildiv = lambda x, d: x // d if (x % d == 0) else x // d + 1

flush = lambda: stdout.flush()
stdstr = lambda: stdin.readline()
stdint = lambda: int(stdin.readline())
stdprint = lambda x: stdout.write(str(x))

mod = 1000000007

# sys.setrecursionlimit(100000000)


# for input and output
if os.path.isfile("input.txt") and os.path.isfile("output.txt"):
    sys.stdin, sys.stdout = open("input.txt", "r"), open("output.txt", "w")

# main code
if __name__ == "__main__":
    pass
