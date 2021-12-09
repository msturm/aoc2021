#!/usr/bin/env python3
from collections import Counter
file1 = '7.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
input = [int(x) for x in input[0].split(',')]

min_fuel1 = 10000000000000000000
min_fuel2 = 10000000000000000000
sum_of_fuel = {}

for x in range(0, 10000):
    if x == 0:
        sum_of_fuel[0] = 0
    elif x == 1:
        sum_of_fuel[1] = 1
    else:
        sum_of_fuel[x] = sum_of_fuel[x - 1] + x


for x in range(0, max(input)):
    fc1 = 0
    fc2 = 0
    for v in input:
        dist = abs(v - x)
        fc1 += dist
        fc2 += sum_of_fuel[dist]
    if min_fuel1 > fc1:
        min_fuel1 = fc1
    if min_fuel2 > fc2:
        min_fuel2 = fc2

print(min_fuel1)
print(min_fuel2)
# part 1: 15 minutes
# part 2: 15 minutes
