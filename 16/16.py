#!/usr/bin/env python3
file1 = '16.in'
import math

input = [x.strip() for x in open(file1, 'r').readlines()][0]
# input = "D2FE28"  # literal
# input = "EE00D40C823060" # 11 bit operator
# input = "38006F45291200" # 15 bit operator
# input = "8A004A801A8002F478" # example 1
# input = "620080001611562C8802118E34" # example 2
# input = "C0015000016115A2E0802F182340" # example 3
# input = "A0016C880162017C3686B18A3D4780" # example 4

# input = "9C0141080250320F1802104A08" # example sum
bininp = bin(int(input, 16))[2:].zfill(4 * len(input))
ans = 0
pc = 0
def parsepacket(p):
    global ans, pc
    # print(p[pc:])
    header = p[pc:pc + 3]
    pc += 3
    version = int(header, 2)
    ans += version
    ptype = p[pc:pc+3]
    pc += 3
    type_desc = ""
    value = ""

    if ptype == "100": #literal
        # print("literal", p[pc:])
        type_desc = "literal"
        nr_part = p[pc:pc+5]
        nr = nr_part[1:]
        pc += 5

        while nr_part[0] == '1':
            nr_part = p[pc:pc+5]
            nr += nr_part[1:]
            pc += 5
        value = str(int(nr, 2))
        print("literal val:", value)
        return int(value)

    else: # operator
        V = []
        type_desc = "operator"
        if p[pc:pc+1] == '1': #11 bits
            pc += 1
            sp_count = p[pc:pc+11]
            pc += 11
            value = str(int(sp_count, 2))
            print("op 11 bit", value, "items")

            for _ in range(int(value)):
                V.append(parsepacket(p))
        elif p[pc:pc+1] == '0': # 15 bits, length of subpackage
            print("op 15 bit")
            pc += 1
            sp_length = p[pc:pc+15]
            pc += 15
            value = str(int(sp_length, 2))
            pend = pc + int(value)
            print("op 15 bit", value, "length")
            while pc < pend:
                V.append(parsepacket(p))

        type_id = int(ptype, 2)
        if type_id == 0:
            return sum(V)
        elif type_id == 1:
            return math.prod(V)
        elif type_id == 2:
            return min(V)
        elif type_id == 3:
            return max(V)
        elif type_id == 5:
            assert len(V) == 2
            return 1 if V[0] > V[1] else 0
        elif type_id == 6:
            assert len(V) == 2
            return 1 if V[0] < V[1] else 0
        elif type_id == 7:
            assert len(V) == 2
            return 1 if V[0] == V[1] else 0
    print(version, ptype, type_desc, value)

print("p2", parsepacket(bininp))
print("p1", ans)
