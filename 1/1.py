#!/usr/bin/env python3
file1 = '1.in'
count1, count2 = 0, 0
depths = [int(x.strip()) for x in open(file1, 'r').readlines()]
# super short version
print("part 1: {0}".format(len([x for x, y in zip(([0] + depths[:-1])[1:], depths[1:]) if x < y])))
print("part 1: {0}".format(len([x for x, y in zip((depths[:1]*3 + depths[:-3])[3:], depths[3:]) if x < y])))


#original version
for n in range(1, len(depths)):
    if depths[n] > depths[n-1]:
        count1 += 1

# in sliding window, 2 elements are always the same, so just compare first from previous and current one
for n in range(3, len(depths)):
    if depths[n] > depths[n - 3]:
        count2 += 1

print("part 1: {0}".format(count1))
print("part 2: {0}".format(count2))
