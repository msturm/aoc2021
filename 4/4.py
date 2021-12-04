#!/usr/bin/env python3
file1 = '4.in'

input = [x.strip() for x in open(file1, 'r').readlines()]

N = [int(x) for x in input[0].split(',')]
print(N)
B = []
board = []
for v in input[2:]:
    if v == '':
        B.append(board)
        board = []
    else:
        vline = [int(x) for x in v.split()]
        board.append(vline)
B.append(board)
best_board = 0
best_board_moment = 1000
best_board_score = 0
worst_board = 0
worst_board_moment = 0
worst_board_score = 0

for boardnum, b in enumerate(B):
    hlines = b
    vlines = []

    for x in range(len(b[0])):
        line = []
        for y in range(len(b)):
            line.append(b[y][x])
        vlines.append(line)

    alllinesBingo = []
    alllines = vlines + hlines
    for line in alllines:
        bl = max([N.index(v) for v in line])
        alllinesBingo.append(bl)

    bingomoment = min(alllinesBingo)
    print("bingo moment {0} after nr: {1}, cur best board moment {2}".format(bingomoment, N[bingomoment], best_board_moment))
    drawn_numbers = N[:bingomoment + 1]
    unmarked_numbers = [x for y in hlines for x in y if x not in drawn_numbers]
    score = sum(unmarked_numbers) * N[bingomoment]
    print("drawn_numbers {0}".format(drawn_numbers))
    print("sum unmarked_numbers {0}".format(sum(unmarked_numbers)))

    if best_board_moment > bingomoment:
        best_board_moment = bingomoment
        best_board = boardnum
        best_board_score = score

    if worst_board_moment < bingomoment:
        worst_board_moment = bingomoment
        worst_board = boardnum
        worst_board_score = score

    # winning_board = alllinesBingo.index(bingomoment)

# winning board
print("board count: {0}".format(len(B)))
print("best board: {0}".format(best_board))
print("P1: " + str(best_board_score))

print("worst board: {0}".format(worst_board))
print("P2: " + str(worst_board_score))
