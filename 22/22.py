#!/usr/bin/env python3
file1 = '22.in'

G_ON = []

def calc_points(cube, p2 = True):
    (x1, y1, z1, x2, y2, z2) = cube
    # for x in range(x1, x2+1):
    #     for y in range(y1, y2+1):
    #         for z in range(z1, z2+1):
    #             print(x, y, z)
    if p2 or (-50 <= x1 <= 50 and -50 <= y1 <= 50 and -50 <= z1 <= 50 and -50 <= x2 <= 50 and -50 <= y2 <= 50 and -50 <= z2 <= 50):
        # print(cube, (x2-x1+1)*(y2-y1+1)*(z2-z1+1))
        return (x2-x1+1)*(y2-y1+1)*(z2-z1+1)
    else:
        return 0

def add_cube(cube, status):
    global G_ON
    G_NEW = []
    (x1, y1, z1, x2, y2, z2) = cube
    if len(G_ON) == 0 and status == 'on':
        G_NEW.append(cube)
        G_ON = G_NEW
    else:
        for (xo1, yo1, zo1, xo2, yo2, zo2) in G_ON:
            intersect = (xo1 <= x2 and yo1 <= y2 and zo1 <= z2) and (x1 <= xo2 and y1 <= yo2 and z1 <= zo2)
            # print(intersect, (xo1 <= x2 and yo1 <= y2 and zo1 <= z2), (x1 <= xo2 and y1 <= yo2 and z1 <= zo2), x1, y1, z1, x2, y2, z2, xo1, yo1, zo1, xo2, yo2, zo2)
            if not intersect:
                G_NEW.append((xo1, yo1, zo1, xo2, yo2, zo2))

            else:
                # x-axis
                if xo1 <= x2 <= xo2:
                    G_NEW.append((x2 + 1, yo1, zo1, xo2, yo2, zo2))
                    xo2 = x2

                if xo1 <= x1 <= x2:
                    G_NEW.append((xo1, yo1, zo1, x1 - 1, yo2, zo2))
                    xo1 = x1

                # y-axis
                if yo1 <= y2 <= yo2:
                    G_NEW.append((xo1, y2 + 1, zo1, xo2, yo2, zo2))
                    yo2 = y2

                if yo1 <= y1 <= yo2:
                    G_NEW.append((xo1, yo1, zo1, xo2, y1 - 1, zo2))
                    yo1 = y1

                # z-axis
                if zo1 <= z2 <= zo2:
                    G_NEW.append((xo1, yo1, z2 + 1, xo2, yo2, zo2))
                    zo2 = z2

                if zo1 <= z1 <= zo2:
                    G_NEW.append((xo1, yo1, zo1, xo2, yo2, z1 - 1))
                    zo1 = z1

        if status == "on":
            G_NEW.append(cube)
        G_ON = G_NEW

input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
    status = v.split(' ')[0]
    coords = v.split(' ')[1].split(',')
    x1, x2 = [int(a) for a in coords[0].split('=')[1].split('..')]
    y1, y2 = [int(a) for a in coords[1].split('=')[1].split('..')]
    z1, z2 = [int(a) for a in coords[2].split('=')[1].split('..')]

    add_cube((x1, y1, z1, x2, y2, z2), status)

ans = 0
for cube in G_ON:
    ans += calc_points(cube, False)
print("p1", ans)

ans = 0
for cube in G_ON:
    ans += calc_points(cube)
print("p2", ans)

    # print(status, x1, x2, y1, y2, z1, z2)
    # GX[(x1, x2)]=[(y1, y2), (z1, z2)]
    # if status == 'on':
        # on_count += (x2+1-x1)*(y2+1-y1)*(z2+1-z1)


        # print(on_count)
    # assert False
    # if -50 <= x1 <= 50 and -50 <= y1 <= 50 and -50 <= z1 <= 50  and -50 <= x2 <= 50 and -50 <= y2 <= 50 and -50 <= z2 <= 50:
    # for x in range(x1, x2 + 1):
    #     for y in range(y1, y2 + 1):
    #         for z in range(z1, z2 + 1):
    #             if status == 'on':
    #                 G[(x, y, z)] = 1
    #             else:
    #                 G[(x, y, z)] = 0

# print([x for x in G.values()].count(1))
