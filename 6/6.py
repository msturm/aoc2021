#!/usr/bin/env python3
from collections import Counter
file1 = '6.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
input = Counter([int(x) for x in input[0].split(',')])

day = 0
borngivers = [0] * 9
p1 = 0
for k, v in input.items():
    borngivers[k] = v

for day in range(256):
    if day == 80:
        p1 = sum(borngivers)

    borngivers[7] += borngivers[0]
    borngivers.append(borngivers[0])
    borngivers.pop(0)

print("p1: ", p1)
print("p2: ", sum(borngivers))
# p1 10 minutes 53 seconds
# P2 55 minutes 46 seconds
