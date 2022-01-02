#!/usr/bin/env python3
from copy import deepcopy
file1 = '25.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
G = []
for v in input:
    G.append([vv for vv in v])

stable = False
step = 0
NG = deepcopy(G)
while not stable:
    # [print(''.join(x)) for x in G]
    # print("\n")
    stable = True
    for r in range(len(G)):
        for c in range(len(G[0])):
            if G[r][c] == '>':
                if c + 1 < len(G[0]) and G[r][c+1] == '.':
                    NG[r][c] = '.'
                    NG[r][c + 1] = '>'
                    stable = False
                elif c+1 == len(G[0]) and G[r][0] == '.':
                    NG[r][c] = '.'
                    NG[r][0] = '>'
                    stable = False
    G = deepcopy(NG)
    NG = deepcopy(G)
    for r in range(len(G)):
        for c in range(len(G[0])):
            if G[r][c] == 'v':
                if r + 1 < len(G) and G[r+1][c] == '.':
                    NG[r][c] = '.'
                    NG[r+1][c] = 'v'
                    stable = False
                elif r + 1 == len(G) and G[0][c] == '.':
                    NG[r][c] = '.'
                    NG[0][c] = 'v'
                    stable = False
    G = deepcopy(NG)
    print(step)
    step += 1
print("p1", step)
