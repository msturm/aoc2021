#!/usr/bin/env python3
file1 = '1.in'
count1, count2 = 0, 0
depths = [int(x.strip()) for x in open(file1, 'r').readlines()]

for n in range(1, len(depths)):
    if depths[n] > depths[n-1]:
        count1 += 1

# in sliding window, 2 elements are always the same, so just compare first from previous and current one
for n in range(3, len(depths)):
    if depths[n] > depths[n - 3]:
        count2 += 1

print("part 1: {0}".format(count1))
print("part 2: {0}".format(count2))
