#!/usr/bin/env python3
from collections import deque
import statistics
file1 = '10.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
V = []

s1 = 0
s2 = []
points1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
points2 = {')': 1, ']': 2, '}': 3, '>': 4}
for v in input:
    e = deque()
    linescore = 0
    corrupted = False
    for c in v:
        if c == '{':
            e.append('}')
        elif c == '[':
            e.append(']')
        elif c == '(':
            e.append(')')
        elif c == '<':
            e.append('>')
        else:
            expected = e.pop()
            if (c == '}' and expected != '}') or \
                (c == ']' and expected != ']') or \
                (c == ')' and expected != ')') or \
                (c == '>' and expected != '>'):
                s1 += points1[c]
                corrupted = True

    if not corrupted:
        if len(e) > 0:
            while e:
                linescore = (linescore * 5) + points2[e.pop()]
        s2.append(linescore)
print(len(s2))

print("p1", s1)
# p1 solved in 10 minutes 46 secons
print("p1", statistics.median(s2))
# p2 solved in 15 minutes 53
