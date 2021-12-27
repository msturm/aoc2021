#!/usr/bin/env python3
file1 = '21.in'
wins = []

p_pos = [6, 2]
# p_pos = [4, 8]
C = {}

def play2(pos1, pos2, score1, score2):
    ans2 = (0, 0)
    if (pos1, pos2, score1, score2) in C:
        return C[(pos1, pos2, score1, score2)]
    if score1 >= 21:
        return (1, 0)
    if score2 >= 21:
        return (0, 1)

    for die1 in [1, 2, 3]:
        for die2 in [1, 2, 3]:
            for die3 in [1, 2, 3]:
                new_pos = pos1 + die1 + die2 + die3
                new_pos %= 10
                if new_pos == 0:
                    new_pos = 10
                new_score = score1 + new_pos + 1
                x, y = play2(pos2, new_pos, score2, new_score)
                ans2 = (ans[0] + y, ans[1] + x)
    C[(pos1, pos2, score1, score2)] = ans2
    return ans2

# print(play2(p_pos[0], p_pos[1], 0, 0))

def play():
    p_score = [0, 0]
    DIE = 0
    # nr_of_rolls = 0
    p = 0
    while p_score[0] < 21 and p_score[1] < 21:
        move = 0
        for _ in range(3):
            DIE = 1 + DIE if DIE < 3 else 1
            move += DIE
            # nr_of_rolls += 1
        p_pos[p] = p_pos[p] + move
        p_pos[p] %= 10
        if p_pos[p] == 0:
            p_pos[p] = 10
        # print(p, p_pos[p])
        p_score[p] += p_pos[p]
        # rounds += 1
        p = 0 if p == 1 else 1

    ans = 0
    for x in p_score:
        if x < 1000:
            print(x, nr_of_rolls)
            ans = x * nr_of_rolls
    return ans
# print(rounds, p_pos, p_score)
print(play)
