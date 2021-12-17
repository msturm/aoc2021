#!/usr/bin/env python3
file1 = '17.in'

TX = (155, 182)
TY = (-117, -67)
# TX = (20, 30)
# TY = (-10, -5)


def shoot():
    global TX, TY
    ans = 0
    ans2 = 0
    steps = 0
    for VX in range(0, TX[1] + 1):
        for VY in range(TY[0], 500):
            hit = False
            max_y = 0
            (x, y) = (0, 0)
            (dx, dy) = (VX, VY)
            # res = hit(x, y)

            while x <= TX[1] and y >= TY[1]:
                steps += 1
                x += dx
                y += dy
                max_y = max(y, max_y)
                if dx > 0:
                    dx -= 1
                elif dx < 0:
                    dx += 1
                dy -= 1

                if not hit and TX[0] <= x <= TX[1] and TY[0] <= y <= TY[1]:
                    ans2 += 1
                    hit = True
            if hit:
                # print(VX, VY, max_y, ans)
                if ans < max_y:
                    ans = max_y
    print(steps)
    return (ans, ans2)

res = shoot()
print("p1", res[0])
print("p2", res[1])


