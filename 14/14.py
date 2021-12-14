#!/usr/bin/env python3
from collections import Counter
from collections import defaultdict
file1 = '14.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
E = input[0]
S = {}
step = 0
char_counter = defaultdict(int)
P = defaultdict(int)
for x in range(len(E)):
    if len(E[x:x+2]) > 1:
        P[E[x:x+2]] += 1

for x in input[0]:
    char_counter[x] += 1
print("start", P)
for v in input[2:]:
    s, m = v.split(' -> ')
    S[s] = m
print(S)

ans1 = 0

while step < 40:
    new_P = {}
    print(step)
    print(P)
    for k, v in P.items():
        if k in S:
            if S[k] == 'K':
                print(k, v)
            char_counter[S[k]] += v
            newKs = [k[0] + S[k], S[k] + k[1]]
            for k in newKs:
                if k in new_P:
                    new_P[k] += v
                else:
                    new_P[k] = v
    P = new_P
    if step == 9:
        ans1 = max(char_counter.values()) - min(char_counter.values())

    #
    # NE = ''
    # for x in range(0, len(E)):
    #     if E[x:x+2] in S and S[E[x:x+2]] == 'K': print(E[x:x+2])
    #     if E[x:x+2] in S:
    #         NE += E[x:x+1] + S[E[x:x+2]]
    #     else:
    #         NE += E[x:x+1]
    #     # print(x, E[x:x+2],  NE)
    # # print(Counter(E))
    # # print("step", step + 1, max(Counter(E).values()), min(Counter(E).values()))
    # print(NE)
    # E = NE

    step += 1



# print({x: Counter(E)[x] for x in sorted(Counter(E).keys())})
# ans1 = max(Counter(E).values()) - min(Counter(E).values())
print("p1", ans1)
# print(P)
print("p2", max(char_counter.values()) - min(char_counter.values()))

# P1 38 minutes
# P2 too long
