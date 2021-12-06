#!/usr/bin/env python3
file1 = '5.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
grid = {}
grid2 = {}
for v in input:
    a1, a2 = [x for x in v.split(' -> ')]
    x1,y1 = [int(x) for x in a1.split(',')]
    x2,y2 = [int(x) for x in a2.split(',')]
    print(x1, y1, x2, y2)
    if x1 == x2:
        if y2 > y1:
            for a in range(y1, y2 + 1):
                if (a, x1) not in grid:
                    grid[(a, x1)] = 1
                else:
                    grid[(a, x1)] +=1

                if (a, x1) not in grid2:
                    grid2[(a, x1)] = 1
                else:
                    grid2[(a, x1)] +=1
        else:
            for a in range(y2, y1 + 1):
                if (a, x1) not in grid:
                    grid[(a, x1)] = 1
                else:
                    grid[(a, x1)] +=1

                if (a, x1) not in grid2:
                    grid2[(a, x1)] = 1
                else:
                    grid2[(a, x1)] +=1

    elif y1 == y2:
        if x2 > x1:
            for a in range(x1, x2 + 1):
                if (y1, a) not in grid:
                    grid[(y1, a)] = 1
                else:
                    grid[(y1, a)] +=1

                if (y1, a) not in grid2:
                    grid2[(y1, a)] = 1
                else:
                    grid2[(y1, a)] +=1
        else:
            for a in range(x2, x1 + 1):
                if (y1, a) not in grid:
                    grid[(y1, a)] = 1
                else:
                    grid[(y1, a)] +=1

                if (y1, a) not in grid2:
                    grid2[(y1, a)] = 1
                else:
                    grid2[(y1, a)] +=1

    elif abs(x1-x2) == abs(y1-y2):
        sx = x1 if y1 < y2 else x2
        ex = x2 if y1 < y2 else x1
        sy = y1 if y1 < y2 else y2
        ey = y2 if y1 < y2 else y1
        print("diag", sy, sx, ey, ex)
        if sx < ex:
            b = sx
            for a in range(sy, ey+1):
                print(a, b)
                if (a, b) not in grid2:
                    grid2[(a, b)] = 1
                else:
                    grid2[(a, b)] +=1
                b+=1
        else:
            b = sx
            for a in range(sy, ey+1):
                print(a, b)
                if (a, b) not in grid2:
                    grid2[(a, b)] = 1
                else:
                    grid2[(a, b)] +=1
                b-=1

# print(grid)

p1 = len([x for x in grid.values() if x > 1])
p2 = len([x for x in grid2.values() if x > 1])
print("p1: {0}".format(p1))
# print(grid2)
print("p2: {0}".format(p2))
# p1 30 minutes

