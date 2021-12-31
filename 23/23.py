#!/usr/bin/env python3
from copy import deepcopy
import sys
sys.setrecursionlimit(int(1e5))
file1 = '23.in'

#############
#...........#
###B#B#D#A###
  #D#C#B#A#
  #D#B#A#C#
  #D#C#A#C#
  #########

A = ['B', 'D', 'D', 'D']
B = ['B', 'C', 'B', 'C']
C = ['D', 'B', 'A', 'A']
D = ['A', 'A', 'C', 'C']

# A = ['B', 'D', 'D', 'A']
# B = ['C', 'C', 'B', 'D']
# C = ['B', 'B', 'A', 'C']
# D = ['D', 'A', 'C', 'A']

# A = ['B', 'A']
# B = ['C', 'D']
# C = ['B', 'C']
# D = ['D', 'A']


HW = [''] * 11
# DP = {}
cost_per_step = {'D': 1000, 'C': 100, 'B': 10, 'A': 1}

START_STATE = (HW, {'A': A, 'B': B, 'C': C, 'D': D}, 0)

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#       A     B     C     D
ROOM_IDX = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
DP = {}
ROOM_SIZE = len(A)

def complete(state):
    (hw, rooms, cost) = state
    for k, v in rooms.items():
        for vv in v:
            if k != vv:
                return False
    return True


def can_move_to_room(e, state):
    global ROOM_IDX
    (hw, rooms, cost) = state
    if hw[e] != '':
        target_idx = ROOM_IDX[hw[e]]

        # is room empty or only contains correct items?
        if all([x=='' or x==hw[e] for x in rooms[hw[e]]]):
            if e < target_idx: # move from left to right
                return all([hw[idx] == '' for idx in range(e + 1, target_idx)])
            else: # move from right to left
                return all([hw[idx] == '' for idx in range(target_idx, e)])
    return False


def move_to_room(e, state):
    global ROOM_IDX
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    #       A     B     C     D
    (hw, rooms, cost) = state
    new_hw = list(hw)
    new_rooms = deepcopy(rooms)
    new_cost = cost
    target_room = hw[e]
    for x in range(ROOM_SIZE -1, -1, -1):
        if rooms[target_room][x] == '':
            new_rooms[target_room][x] = hw[e]
            stepcost = cost_per_step[hw[e]]
            move_cost = (stepcost * (x+1)) + (stepcost * abs(ROOM_IDX[hw[e]] - e))
            new_cost += move_cost
            new_hw[e] = ''
            print(f'Move {hw[e]} to room from hw idx {e} to room {target_room} pos {x} cost {move_cost}')
            print(new_hw, new_rooms, new_cost)
            # print(new_hw, new_rooms, new_cost)
            return new_hw, new_rooms, new_cost
    assert False


def move_to_hw(r, e, state):
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    #       A     B     C     D
    (hw, rooms, cost) = state
    new_hw = list(hw)
    new_rooms = deepcopy(rooms)
    new_cost = cost
    for x in range(0, ROOM_SIZE):
        if new_rooms[r][x] != '':
            new_hw[e] = new_rooms[r][x]
            new_rooms[r][x] = ''
            stepcost = cost_per_step[new_hw[e]]
            move_cost = (stepcost * (x+1)) + (stepcost * abs(ROOM_IDX[r] - e))
            new_cost += move_cost
            # print(new_hw, new_rooms, new_cost)
            print(f'Move item {new_hw[e]} from room {r} pos {x} to hw idx {e}; cost {move_cost}')
            print(new_hw, new_rooms, new_cost)
            return new_hw, new_rooms, new_cost
    assert False

def room_has_items(r, state):
    (hw, rooms, cost) = state
    return not all([x == '' for x in rooms[r]])

def can_move_to_hw(r, e, state):
    global ROOM_IDX
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    #       A     B     C     D
    (hw, rooms, cost) = state
    if e in [2, 4, 6, 8] or hw[e] != '':
        return False
    elif all([x=='' or x==r for x in rooms[r]]):
        return False
    else:
        start_idx = ROOM_IDX[r]
        end_idx = e
        if start_idx < end_idx:  # move from left to right
            return all([hw[x] == '' for x in range(start_idx, end_idx)])
        else:  # move from right to left
            return all([hw[x] == '' for x in range(end_idx, start_idx)])

ans = 1e9
def solve(state):
    global DP, ans
    # print(state)
    (hw, rooms, cost) = state

    key = (tuple((k, tuple(v)) for k,v in rooms.items()), tuple(hw))
    # print(len(DP))
    if key not in DP or DP[key] > cost:
        print(state)
        DP[key] = cost
    else:
        return ans

    if complete(state):
        print("THERE IS A COMPLETE STATE", state)
        DP[key] = cost
        ans = min(ans, cost)
        return ans
    else:
        # new_states = []
        # solve in new state where 1 item is moved from hw to a room
        for k, e in enumerate(hw):
            if can_move_to_room(k, state):
                # move_to_room(k, state)
                # new_states.append(move_to_room(k, state))
                return solve(move_to_room(k, state))
        new_states = []
        for r in rooms:
            for k, e in enumerate(hw):
                if room_has_items(r, state) and can_move_to_hw(r, k, state):
                    # move_to_hw(r, k, state)
                    new_states.append(move_to_hw(r, k, state))
        if len(new_states) == 0:
            return int(1e9)
        else:
            return min([solve(ns) for ns in new_states])
        # if len(new_states) == 0:
        #     DP[key] = int(1e9)
        #     return int(1e9)
        # else:
        #     min_cost = min([solve(ns) for ns in new_states])
        #     return min_cost
print(solve(START_STATE))

