#!/usr/bin/env python3
from collections import Counter
file1 = '12.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
C = {}
ans = 0
ans1 = 0
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
    global C, ans, ans1
    if cave != 'end':
        for c in C[cave]:
            if c.isupper():
                visit(c, path + [cave], dbl_sc)
            elif c.islower() and c not in path:
                visit(c, path + [cave], dbl_sc)
            elif c.islower() and c != 'start' and c != 'end' and dbl_sc == '':
                visit(c, path + [cave], c)

    else:
        ans += 1
        if not dbl_sc:
            # part 1
            ans1 += 1

visit('start', [])
print("P1", ans1)
print("P2", ans)
# P1 26 min 46 sec
# P2 more than 1,5 hour

