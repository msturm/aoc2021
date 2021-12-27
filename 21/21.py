#!/usr/bin/env python3
file1 = '21.in'

p_pos = [6, 2]
# p_pos = [4, 8]
p_score = [0, 0]
DIE = 0
nr_of_rolls = 0

rounds = 0
p = 0
while p_score[0] < 1000 and p_score[1] < 1000:
    move = 0
    for _ in range(3):
        DIE = 1 + DIE if DIE < 100 else 1
        move += DIE
        nr_of_rolls += 1
    p_pos[p] = p_pos[p] + move
    p_pos[p] %= 10
    if p_pos[p] == 0:
        p_pos[p] = 10
    # print(p, p_pos[p])
    p_score[p] += p_pos[p]
    rounds += 1
    p = 0 if p == 1 else 1

ans = 0
for x in p_score:
    if x < 1000:
        print(x, nr_of_rolls)
        ans = x * nr_of_rolls
# print(rounds, p_pos, p_score)
print(ans)
