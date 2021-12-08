#!/usr/bin/env python3
file1 = '8.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
count = 0
outputsum = 0
#  11
# 2  3
#  44
# 5  6
#  77

for v in input:
    inp = v.split("|")[0].strip().split()
    outp = v.split("|")[1].strip().split()

    D = {}
    P = {}
    while len(P) < 10:
        for u in inp:
            v = "".join(sorted(u))
            print(P)
            if len(v) == 2:
                P[1] = v
            if len(v) == 3:
                P[7] = v
            if len(v) == 4:
                P[4] = v
            if len(v) == 7:
                P[8] = v
            if len(v) == 5:
                if 1 in P and all([x in v for x in P[1]]):
                    P[3] = v
                elif 6 in P and all([x in P[6] for x in v]):
                    P[5] = v
                elif 3 in P and 5 in P and v != P[3] and v != P[5]:
                    P[2] = v
            if len(v) == 6:
                if 4 in P and all([x in v for x in P[4]]):
                    P[9] = v
                elif 7 in P and all([x in v for x in P[7]]):
                    P[0] = v
                elif 0 in P and 9 in P and v != P[0] and v != P[9]:
                    P[6] = v

    cursum = ""
    Q = {y:x for x,y in P.items()}
    for u in outp:
        v = "".join(sorted(u))
        cursum += str(Q[v])
        if len(v) in [2, 4, 3, 7]:
            count += 1
    outputsum += int(cursum)
print("p1", count)
print("p2", outputsum)
