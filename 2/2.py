#!/usr/bin/env python3
file1 = '2.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
hpos = 0
depth = 0

for v in input:
    dir, a = v.split(" ")
    if dir == 'forward':
        hpos += int(a)
    elif dir == 'down':
        depth += int(a)
    elif dir == 'up':
        depth -= int(a)

print("p1: {0}".format(hpos*depth))

#part2
hpos = 0
depth = 0
aim = 0
for v in input:
    dir, a = v.split(" ")
    if dir == 'forward':
        hpos += int(a)
        depth += aim * int(a)
    elif dir == 'down':
        aim += int(a)
    elif dir == 'up':
        aim -= int(a)
print("p2: {0}".format(hpos*depth))
