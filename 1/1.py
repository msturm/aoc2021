#!/usr/bin/env python3
file1 = '1.in'

count = 0
count2 = 0
prev = -1
psum = 0
with open(file1, 'r') as f:
    elem = [int(x.strip()) for x in f.readlines()]
    for v in elem:
        if v > prev:
            count += 1
        prev = v

    for n in range(2, len(elem)):

        w = elem[n-2] + elem[n-1] + elem[n]
        if w > psum:
            count2 += 1
        psum = w

print("part 1: {0}".format(count-1))
print("part 2: {0}".format(count2-1))
