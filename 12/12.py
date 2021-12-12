#!/usr/bin/env python3
from collections import Counter
file1 = '12.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
C = {}
N = []
V = []
P = set()
ans = 0
for v in input:
    n1, n2 = v.split('-')
    if n1 not in C:
        C[n1] = [n2]
    else:
        C[n1] += [n2]
    if n2 not in C:
        C[n2] = [n1]
    else:
        C[n2] += [n1]
print(C)

def visit(cave, path, dbl_sc = ''):
    global C, V, ans
    # print(cave)
    if cave != 'end':
        V.append(cave)
        smallcaves = [p for p in path if p.islower()]
        for c in C[cave]:
            if c.isupper():
                visit(c, path + [cave], dbl_sc)
            elif c.islower() and c not in smallcaves:
                smallcaves.append(c)
                visit(c, path + [cave], dbl_sc)
            elif c.islower() and c in smallcaves and c != 'start' and c != 'end' and dbl_sc == '':
                smallcaves.append(c)
                visit(c, path + [cave], c)
            # elif c.islower() and  c in smallcaves and dbl_sc == c:
            #     smallcaves.append(c)
            #     visit(c, path + [cave], c)

    else:
        ans += 1
        P.add("".join(path))
        # print(path + ['end'])


visit('start', [])
print(ans)
print(len(P))
# P1 26 min 46 sec
# P2 more than 1,5 hour

