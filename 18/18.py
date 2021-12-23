#!/usr/bin/env python3
import ast
import math

file1 = '18.in'

input = [x.strip() for x in open(file1, 'r').readlines()]

pairs = []
for v in input:
    # pairs.append(ast.literal_eval(v))
    pairs.append(v)


def explode(p):
    pc = 0
    depth_counter = 0
    last_left_start_idx = -1
    next_right_start_idx = -1
    last_left_value = 0
    next_right_value = 0
    while pc < len(p):
        # print("pc", pc, p[pc:], depth_counter)
        if p[pc] == '[':
            depth_counter += 1
        elif p[pc] == ']':
            depth_counter -= 1
        elif p[pc].isnumeric():
            last_left_start_idx = pc
            last_left_end_idx = pc+1
            while p[last_left_end_idx].isnumeric():
                last_left_end_idx += 1
            last_left_value = int(p[last_left_start_idx:last_left_end_idx])
            pc = last_left_end_idx - 1

        if depth_counter == 4: # next pair explodes
            backtrack_idx = pc
            pc += 1
            explode_start_idx = pc
            if p[pc].isnumeric():
                last_left_start_idx = pc
                last_left_end_idx = last_left_start_idx + 1
                while p[last_left_end_idx].isnumeric():
                    last_left_end_idx += 1
                last_left_value = int(p[last_left_start_idx:last_left_end_idx])
            if p[pc] == '[':
                explode_start_idx = pc
                explode_end_idx = pc
                while p[explode_end_idx] != ']':
                    explode_end_idx += 1
                explode_pair = [int(x) for x in p[pc+1:explode_end_idx].split(',')]
                explode_end_idx += 1

                # find right number
                for x in range(explode_end_idx, len(p)):
                    if p[x].isnumeric():
                        next_right_start_idx = x
                        break


                if next_right_start_idx > 0:
                    next_right_end_idx = next_right_start_idx + 1
                    while p[next_right_end_idx].isnumeric():
                        next_right_end_idx += 1
                    next_right_value = int(p[next_right_start_idx:next_right_end_idx])

                # print(p, "explode", explode_pair)

                # do the actual explosion
                if last_left_start_idx == -1 and next_right_start_idx > 0: # no left
                    return p[0:explode_start_idx] + "0" + p[explode_end_idx:next_right_start_idx] + str(next_right_value + explode_pair[1]) + p[next_right_end_idx:]
                elif last_left_start_idx > 0 and next_right_start_idx == -1: #no right
                    return p[0:last_left_start_idx] + str(last_left_value + explode_pair[0]) + p[last_left_end_idx:explode_start_idx] + "0" + p[explode_end_idx:]
                else:
                    # print(explode_start_idx, explode_end_idx, next_right_idx, p[explode_start_idx:])
                    #print('q', last_left_value, last_left_start_idx, p[0:last_left_start_idx], next_right_value)
                    if p[explode_start_idx-1] != ',':
                        return p[0:last_left_start_idx] + str(last_left_value + explode_pair[0]) + p[last_left_end_idx:explode_start_idx] + "0" + p[explode_end_idx:next_right_start_idx] + str(next_right_value + explode_pair[1]) + p[next_right_end_idx:]
                    else:
                        return p[0:last_left_start_idx] + str(last_left_value + explode_pair[0]) + p[last_left_end_idx:explode_start_idx] + "0" + p[explode_end_idx:next_right_start_idx] + str(next_right_value + explode_pair[1]) + p[next_right_end_idx:]
            else: # no explosion
                pc = backtrack_idx

        pc += 1
    return False

def split(p):
    pc = 0
    while pc < len(p):
        if p[pc].isnumeric():
            split_start_idx = pc
            split_end_idx = pc+1
            while p[split_end_idx].isnumeric(): # two digits
                split_end_idx += 1
            if int(p[split_start_idx:split_end_idx]) > 9:
                split_value = int(p[split_start_idx:split_end_idx])
                split_l_value = math.floor(split_value/2)
                split_r_value = math.ceil(split_value/2)
                return p[0:split_start_idx] + "[" + str(split_l_value) + "," + str(split_r_value) + "]" + p[split_end_idx:]
        pc += 1
    return False

# print(pairs)
# 18.test
# print("explode", pairs[0], '->', explode(pairs[0]))
# print("explode", pairs[1], '->', explode(pairs[1]))
# print("explode", pairs[2], '->', explode(pairs[2]))
# print("explode", pairs[3], '->', explode(pairs[3]))
# print("explode", pairs[4], '->', explode(pairs[4]))
#
# 18.test
# v = pairs[5]
#
# v = explode(pairs[5])
# print("explode", pairs[5], '->', v)
# v = explode(v)
# print("explode", v)
# v = split(v)
# print("split", v)
# v = split(v)
# print("split", v)
# v = explode(v)
# print("explode", v)


# print("\n\n")
def reduce(v):
    change = True
    while change:
        change = False
        oldv = v
        v = explode(v)
        if v:
            change = True
            # print("explode", oldv, '->', v)
        if not v:
            v = split(oldv)
            if v:
                change = True
                # print("split", oldv, '->', v)
    return oldv

def magnitude(p):
    pc = 0
    if p[pc+1].isnumeric(): #left is number
        left_start = pc + 1
        left_end = pc + 2
        left_value = -1
        while p[left_end] != ',':
            left_end += 1
        left_value = p[left_start:left_end]
        pc = left_end
    # else: # left is pair
    #     depth = 0
    #     pc += 1
    else:
        left_start = pc + 1
        pc += 2
        depth = 1
        while depth > 0:
            if p[pc] == '[':
                depth += 1
            if p[pc] == ']':
                depth -= 1
            pc += 1
        left_end = pc
        left_value = magnitude(p[left_start:left_end])
        # print(left_value)
    if p[pc + 1].isnumeric(): # right number
        right_start = pc + 1
        right_end = pc + 2
        right_value = -1
        while p[right_end] != ']':
            right_end += 1
        right_value = p[right_start:right_end]
        pc = right_end
    else:
        right_start = pc + 1
        pc += 2
        depth = 1
        while depth > 0:
            if p[pc] == '[':
                depth += 1
            if p[pc] == ']':
                depth -= 1
            pc += 1
        right_end = pc
        right_value = magnitude(p[right_start:right_end])
        # print(right_value)
    return 3*int(left_value) + 2*int(right_value)

# print(explode("[[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[11,9],[0,[11,8]]]]]"))
# print(reduce("[[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]],[1,[[[9,3],9],[[9,0],[0,7]]]]]"))
# print("[[[[13,7],[14,12]],[[10,0],15]],[1,[[[9,3],9],[[9,0],[0,7]]]]]")
# print(explode("[[[[13,7],[14,12]],[[10,0],15]],[1,[[[9,3],9],[[9,0],[0,7]]]]]"))

# print(magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"))


def add(p1, p2):
    return "[" + p1 + "," + p2 + "]"


def part1():
    result = pairs[0]
    for x in pairs[1:]:
        # print(result, x)
        result = add(result, x)
        # print(result)
        result = reduce(result)
        # print("result", result)
    return magnitude(result)

print("p1", part1())

def part2():
    max_magnitude = 0
    for x in pairs:
        for y in pairs:
            if x != y:
                result = add(x, y)
                result = reduce(result)
                result = magnitude(result)
                max_magnitude = max(result, max_magnitude)
    return max_magnitude

print(part2())





# def count_list(l):
#     count = 0
#     for e in l:
#         if isinstance(e, list):
#             count += 1 + count_list(e)
#     return count
#
# def explode(l, d=0, left = -1, right = -1):
#     if d == 4:
#         print("explode ", l, left, right)
#     if isinstance(l[0], int) and isinstance(l[1], int):
#         return [l[0], l[1]]
#     elif isinstance(l[0], list) and isinstance(l[1], list):
#         # find right nr:
#         right_nr = find_first_num(l[1])
#         left_nr = find_first_num(l[0])
#         return (explode(l[0], d+1, left, right_nr), explode(l[1], d+1, left_nr, right))
#     elif isinstance(l[0], list): # there is a 'right' int, left explodes
#         return exp
#         lode(l[0], d+1, left, l[1])
#     elif isinstance(l[1], list): # there is a 'left' int
#         return explode(l[1], d+1, l[0], right)
#
# def find_first_num(l):
#     for e in l:
#         if isinstance(e, int):
#             return e
#         else:
#             return find_first_num(e)
#
# def has_nested_list(l):
#     answer = False
#     for e in l:
#         if isinstance(e, list):
#             answer = True
#     return answer
#
#
# for p in pairs:
#     # find_pair(p)
#     print(find_pair(p))



