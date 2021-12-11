#!/usr/bin/env python3
file1 = '11.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
G = {}
for r, l in enumerate(input):
    for c, v in enumerate(l):
        G[(r, c)] = int(v)

steps = 0
cc = len(input[0])
rc = len(input)
D = [-1, 0, 1]
ans = 0
ans2 = 0
while steps < 100000:
    print(steps)
    for k in G:
        G[k] += 1
    F = []
    update = True
    while update:
        update = False
        for (r, c) in G.keys():
            if G[(r, c)] > 9 and (r, c) not in F:
                F.append((r,c))
                ans += 1
                update = True
                for dr in D:
                    for dc in D:
                        if 0 <= r+dr < rc and 0 <= c+dc < cc:
                            G[(r+dr, c+dc)] += 1
    for (r, c) in G.keys():
        if G[(r, c)] > 9:
            G[(r, c)] = 0

    for r in range(rc):
        print("".join([str(G[(r, c)]) for c in range(cc)]))

    if sorted(G.keys()) == sorted(F):
        ans2 = steps
        break
    steps += 1
print("p1", ans)
# P1 41 min 51 sec
print("p2" , ans2 + 1)
# P2 2 minutes
