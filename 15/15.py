#!/usr/bin/env python3
import sys, heapq
file1 = '15.in'

G = []
input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
    G.append([int(x) for x in v])


def creategrid(tr, tc, G):
    G2 = []
    R = len(G)
    C = len(G[0])
    for r in range(tr + 1):
        for c in range(tc + 1):
            v = G[r % R][c % C] + r//len(G) + c//len(G[0])
            if v > 9:
                v -= 9

            if r == len(G2):
                G2.append([v])
            else:
                G2[r].append(v)
    return G2


def ssp(tr, tc, G):
    G2 = creategrid(tr, tc, G)
    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]

    Q = []
    S = {}
    heapq.heappush(Q, (0, 0, 0))

    while Q:
        (dist, r, c) = heapq.heappop(Q)

        if (r, c) not in S or S[(r, c)] > dist:
            S[(r, c)] = dist
            # N = neighbour nodes to update
            N = [(r+DR[x], c+DC[x]) for x in range(4) if 0 <= r+DR[x] <= tr and 0 <= c+DC[x] <= tc]
            for n in N:
                (rr, cc) = n
                curdist = dist + G2[rr][cc]
                heapq.heappush(Q, (curdist, rr, cc))

    return S[(tr, tc)]


print("p1", ssp(99, 99, G))
print("p2", ssp(499, 499, G))


