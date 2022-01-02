#!/usr/bin/env python3
file1 = '24.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
P = []

for v in input:
    words = v.split(' ')
    if len(words) == 2:
        (op, par1) = words
        P.append((op, par1, ''))
    else:
        (op, par1, par2) = words
        P.append((op, par1, par2))

def exec(P, nr):
    MEM = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    input = [int(x) for x in str(nr)]
    input_pointer = 0
    # print(input)
    # assert False
    # print("=" * 10)
    for (op, par1, par2) in P:
        # print(MEM, op, par1, par2)
        if par2 in ['w', 'x', 'y', 'z']:
            val2 = MEM[par2]
        elif par2 == '':
            val2 = -1
        else:
            val2 = int(par2)

        if op == 'inp':
            if input_pointer == len(input):
                return MEM
            MEM[par1] = input[ input_pointer]
            input_pointer += 1
        elif op == 'add':
            MEM[par1] = MEM[par1] + val2
        elif op == 'mul':
            MEM[par1] = MEM[par1] * val2
        elif op == 'div':
            MEM[par1] = MEM[par1] // val2
        elif op == 'mod':
            MEM[par1] = MEM[par1] % val2
        elif op == 'eql':
            if MEM[par1] == val2:
                MEM[par1] = 1
            else:
                MEM[par1] = 0
    return MEM



# ans = 99999999999999
# zval = 1
# while zval > 0:
#     print(ans)
#     zval = exec(P, ans)['z']
#     ans -= 1
# print(ans)

# 18 lines per number
#changes on lines 4, 5 and 15
V1 = []
V2 = []
V3 = []
for c, l in enumerate(P):
    if c % 18 == 4:
        V1.append(int(l[2]))
    elif c % 18 == 5:
        V2.append(int(l[2]))
    elif c % 18 == 15:
        V3.append(int(l[2]))
    elif l != P[c-18]:
        assert l == P[c-18], f"line {c}: {l}"

assert len(V1) == 14, f"V1 has too few elements {len(V1)}"
assert len(V2) == 14, "V2 has too few elements"
assert len(V3) == 14, "V3 has too few elements"
[print(V1[x], V2[x], V3[x]) for x in range(len(V1))]


# ((z*V1[pos]) * (26 if ((z % 26) + V2[pos]) != w else 1)) + ((w + V3[pos])*(0 if ((z % 26) + V2[pos]) == w else 1))
counter = 0
ZVAL = [(0, 9, 0)]
ZINP = []
# for pos in range(13, -1, -1):
#     for i in range(9, 0, - 1):
#         # z = ZVAL[(pos - 1, )]
#         z = 0 # start value for z
#         w = i
#         res = 1
#         for z in range(1000000):
#             if res == 0:
#                 ZINP.append(z)
#             res = ((z*V1[pos]) * (26 if ((z % 26) + V2[pos]) != w else 1)) + ((w + V3[pos])*(0 if ((z % 26) + V2[pos]) == w else 1))
#         # ZVAL.append((pos, w, res))
print(ZINP)
# print(ZVAL)

for i in range(1, 10000):
    # print(i, exec(P, i))
    if exec(P, i) == 1:
        print(i, exec(P, i))
# z = 0
# w = 9
# print((z*26) * (26 if ((z%26) +10) != w  else 1))
# print((w+2) * (0 if ((z%26) +10) == w else 1))
# print('calc', ((z*26) * (26 if ((z%26) +10) != w else 1)) + ((w+2)*(0 if ((z%26) +10) == w else 1)))
