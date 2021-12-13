#!/usr/bin/env python3
file1 = '13.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
G = set()
F = []
folds = False
for v in input:
    if len(v) == 0:
        folds = True
        continue

    if not folds:
        c, r = [int(x) for x in v.split(",")]
        G.add((r, c))
    else:
        a, v = [x for x in v.split(' ')[2].split('=')]
        F.append((a, int(v)))


print(sorted(G))
print("folds")
print(F)

for a, v in F:
    print(a, v)
    DG = set()
    if a == 'x':
        # fold left
        for r, c in G:
            if c > v:
                c = v-(c-v)
            DG.add((r, c))
    if a == 'y':
        #fold up
        for r, c in G:
            if r > v:
                r = v-(r-v)
            DG.add((r, c))
    G = DG
    print(sorted(G))
print(len(G))
# P1 35 min 29 sec
ans2 = ""
max_r = max([r for r, c in G])
max_c = max([c for r, c in G])
for r in range(max_r + 1):
    for c in range(max_c + 1):
        if (r, c) in G:
            ans2 += '#'
        else:
            ans2 += ' '
    ans2 += "\n"
print(ans2)
# P2 9 min 18 sec
