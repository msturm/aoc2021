#!/usr/bin/env python3
file1 = '3.in'

# part1  14 minutes 29 sec

input = [x.strip() for x in open(file1, 'r').readlines()]
# count all 1s
w = [0] * (len(input[0]))
total = len(input)

for v in input:
    for i in range(len(v) - 1):
        if v[i] == '1':
            w[i] += 1

#part 2 31 minutes

gamma = ''
epsilon = ''
for x in w:
    if total/2 > x:
       gamma += '0'
       epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print("gamma: {0} {1}".format(gamma, int(gamma, 2)))
print("epsilon: {0} {1}".format(epsilon, int(epsilon, 2)))
print("p1: {0}".format(int(gamma, 2)*int(epsilon, 2)))

og = input.copy()
co = input.copy()
i = 0
while len(og) > 1:
    onecount = len([v[i] for v in og if v[i] == '1'])
    print(onecount)
    bval = '1' if onecount >= len(og)/2 else '0'
    og = [p for p in og if p[i] == bval]
    print(len(og))
    i += 1
print(og)
i = 0
while len(co) > 1:
    zerocount = len([v[i] for v in co if v[i] == '0'])
    print(zerocount)
    bval = '0' if zerocount <= len(co)/2 else '1'
    co = [p for p in co if p[i] == bval]
    print(len(co))
    i += 1
print(co)
print("p2: {0}".format(int(og[0], 2)*int(co[0],2)))
