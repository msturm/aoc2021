#!/usr/bin/env python3
import math
file1 = '9.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
grid = {}
max_r = 0
max_c = 0
r = 0
for v in input:
    for c in range(len(v)):
        grid[(r, c)] = int(v[c])
    r+=1
max_r = r
max_c = len(input[0])
LP = {}

for c in range(max_c):
    for r in range(max_r):
        lowpoint = True
        for dc in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                if r+dr >= 0 and c+dc >= 0 and r+dr < max_r and c+dc < max_c and grid[(r+dr, c+dc)] < grid[(r, c)]:
                    lowpoint = False
        if lowpoint:
            LP[(r, c)] = grid[(r, c)]
rl = 0
for v in LP.values():
    rl += v + 1

BS_sizes = []
in_BS = {}

for lp in LP:
    BS = {}
    prev_size = -1
    while len(BS) > prev_size:
        BS[lp] = grid[lp]
        prev_size = len(BS)
        print(BS, len(BS), prev_size)
        NP = {}
        for k in BS.keys():
            r = k[0]
            c = k[1]
            for dc in [-1, 0, 1]:
                if r >= 0 and c+dc >= 0 and r < max_r and c+dc < max_c and grid[(r, c+dc)] < 9 and (r, c+dc) not in BS:
                    print(r, c+dc, grid[(r, c+dc)])
                    NP[(r, c+dc)] = grid[(r, c+dc)]
            for dr in [-1, 0, 1]:
                if r+dr >= 0 and c >= 0 and r+dr < max_r and c < max_c and grid[(r+dr, c)] < 9 and (r+dr, c) not in BS:
                    NP[(r+dr, c)] = grid[(r+dr, c)]
            print(NP)
        BS.update(NP)
    print(BS)
    BS_sizes.append(len(BS))


print("p1", rl)
print(sorted(BS_sizes, reverse=True)[0:3])
print("p2", math.prod(sorted(BS_sizes, reverse=True)[0:3]))
