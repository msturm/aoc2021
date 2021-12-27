#!/usr/bin/env python3
file1 = '20.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
alg = [x for x in input[0]]

G = []
G = [v for v in input[2:]]
DR = [-1, 0, 1]
DC = [-1, 0, 1]
default_v = '0'
for x in range(50):
    NG = []
    for r in range(-1, len(G)+1):
        new_r = ''
        for c in range(-1, len(G[0]) + 1):
            v = -1
            bv = ''
            for dr in DR:
                for dc in DC:
                    # print(r+dr, len(G), c+dc, len(G[r]))
                    if 0 <= r+dr < len(G) and 0 <= c+dc < len(G[0]):
                        bv += '1' if G[r+dr][c+dc] == '#' else '0'
                    else:
                        bv += default_v
            v = int(bv, 2)
            new_r += alg[v]
        # print(new_r)
        NG.append(new_r)
    default_v = '1' if default_v == '0' else '0'
# print(NG)
#     [print(x) for x in NG]
    G = NG
    # [print(x) for x in G]
    # print("\n")
print("p1", sum([x.count('#') for x in G]))
