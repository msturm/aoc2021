#!/usr/bin/env python3
# file1 = '19.test2'
file1 = '19.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
S = {}
scanner = -1
for v in input:
    if v == '':
        next
    elif v.startswith('--- scanner '):
        scanner = int(v[12:14].strip())
        S[scanner] = []
    else:
        x, y, z = [int(x) for x in v.split(',')]
        S[scanner].append((x, y, z))

def rotateX(x, y, z):
    return (x, z, -y)

def rotateY(x, y, z):
    return (z, y, -x)

def rotateZ(x, y, z):
    return (y, -x, z)

def flipX(x, y, z):
    return (-x, y, z)

def flipY(x, y, z):
    return (x, -y, z)

def flipZ(x, y, z):
    return (x, y, -z)

def permutate(scanner):
    # s = [5, 6, -4]
    # R = {scanner[0]:[]}
    P = [[] for x in range(24)]
    # print("P", len(P))

    for s in scanner:
        # print(s)
        x, y, z = s
        directions = []
        rotation = 0
        for _ in range(4):
            (x, y, z) = rotateY(x, y, z)
            for _ in range(4):
                (x, y, z) = rotateZ(x, y, z)
                directions.append((x, y, z))
                P[rotation].append((x, y, z))
                rotation += 1

        (x, y, z) = rotateX(x, y, z)
        for _ in range(4):
            (x, y, z) = rotateZ(x, y, z)
            directions.append((x, y, z))
            P[rotation].append((x, y, z))
            rotation += 1

        (x, y, z) = rotateX(x, y, z)
        (x, y, z) = rotateX(x, y, z)
        for _ in range(4):
            (x, y, z) = rotateZ(x, y, z)
            directions.append((x, y, z))
            P[rotation].append((x, y, z))
            rotation += 1

        # look directions
        # x, y, z = s
        # directions.append((x, y, z)) # look from -z
        # for _ in range(3):
        #     (x, y, z) = directions[-1]
        #     directions.append((z, y, -x))
        # directions.append((x, z, -y))
        # directions.append((x, -z, y))
        # directions.append((-x, y, -z)) # look from z
        # directions.append((-z, y, x)) # look from -x
        # directions.append((z, y, -x)) # look from x
        # directions.append((x, -z, y)) # look from y
        # directions.append((x, z, -y)) # look from -y
        # rotate
        # for d in directions:
        #     for _ in range(4):
        #         x, y, z = d
        #         d = (y, -x, z)
        #         P[rotation].append((y, -x, z))
        #         rotation += 1
        #
        # print(len(P))
        # [print(x) for x in P]
    # print(P[0][0])
    # print(P[1][0])
    #     [print(x) for x in P]
        # assert False
    return P

# print(S[0])
# permutate(S[0])
# [print(x) for x in permutate(S[1])]
beacons = set() # all beacons
scanner_mapping = {}

def update_mapping_from_0(s1_idx, s2_idx, s2_pos):
    global scanner_mapping
    print("update_mapping", s1_idx, s2_idx, s2_pos)
    new_mapping = -1
    if s1_idx == 0:
        (x2, y2, z2) = s2_pos
        new_mapping = (x2, y2, z2)
    else:
        for (i1, i2) in scanner_mapping:
            if i2 == s1_idx:
                (x1, y1, z1) = scanner_mapping[(0, i2)]
                (x2, y2, z2) = s2_pos
                new_mapping = (x1+x2, y1 + y2, z1 + z2)
    scanner_mapping[(0, s2_idx)] = new_mapping

def trymatch(s1_idx, s2_idx, scanner1, scanner2):
    global scanner_mapping
    (s1x, s1y, s1z) = (0, 0, 0)
    if s1_idx != 0:
        (s1x, s1y, s1z) = scanner_mapping[(0, s1_idx)]

    for (x1, y1, z1) in scanner1:
        for (x2, y2, z2) in scanner2:
            dx, dy, dz = (x1 - x2, y1 - y2, z1 - z2)
            # print(dx, dy, dz)
            mc = 0
            for (x, y, z) in scanner2:
                if (x, y, z) != (x2, y2, z2) and (x+dx, y+dy, z+dz) in scanner1:

                    mc += 1
                    # print('match', c, mc)
            # if len([(x, y, z) for (x, y, z) in scanner2 if (x, y, z) != (x2, y2, z2) and (x+dx, y+dy, z+dz) in scanner1]) >= 11:
            #     print("mc", mc)
            if mc >= 11:
                for (x, y, z) in scanner2:
                    beacons.add((s1x + x + dx, s1y + y + dy, s1z + z + dz))
                return (dx, dy, dz)
    # if len(matches) > 0:
    #     print(len(matches))
    #     return matches[0]

# permutate(S[0])

scanner1 = S[0]
s1_idx = 0
# scanner2 = S[1]
# s2_pms = permutate(scanner2)
matched_scanners = {0: S[0]}

unmatched_scanners = S.copy()
unmatched_scanners.pop(0)
for b in S[0]:
    beacons.add(b)

while len(unmatched_scanners) > 0:
    new_matched_scanners = {}
    for (s1_idx, scanner1) in matched_scanners.items():
        for (s2_idx, scanner2) in unmatched_scanners.items():
            if s1_idx == s2_idx:
                continue
            s2_pms = permutate(scanner2)
            for c, s2_pm in enumerate(s2_pms):
                s2_pos = trymatch(s1_idx, s2_idx, scanner1, s2_pm)
                if s2_pos:
                    S[s2_idx] = s2_pm
                    update_mapping_from_0(s1_idx, s2_idx, s2_pos)
                    # scanner_mapping[(s1_idx, s2_idx)] = s2_pos
                    new_matched_scanners[s2_idx] = s2_pm
                    print(s2_idx, s2_pos)
                    # break

    # add new scanners to matched scanners
    matched_scanners.update(new_matched_scanners)
    print(scanner_mapping)
    # removed found scanners from unmatched scanners
    unmatched_keys = list(unmatched_scanners.keys()).copy()
    for k in unmatched_keys:
        if k in matched_scanners:
            unmatched_scanners.pop(k)
    print("remaining", len(unmatched_scanners.keys()))

prev_i = 0


print("scanner 1", scanner_mapping[(0, 1)])
print("scanner 4", scanner_mapping[(0, 4)])
print("scanner 2", scanner_mapping[(0, 2)])
print("scanner 3", scanner_mapping[(0, 3)])

print("p1", len(beacons))

max_distance = 0
for (x1, y1, z1) in scanner_mapping.values():
    for (x2, y2, z2) in scanner_mapping.values():
        mhd = abs(x1-x2) + abs(y1 - y2) + abs(z1 - z2)
        max_distance = max(mhd, max_distance)
print("p2", max_distance)
# print(scanner1)
# print(scanner2)
# for x in S.items():
#     [print("1", a) for a in permutate(x)[x[0]]]
