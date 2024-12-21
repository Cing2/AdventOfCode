from collections import deque
import copy
import time
from typing import Tuple


def main():
    print("Day 15")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def part1():
    grid, ops = load_input()
    # print(grid, ops)
    # find pos robot
    rpos = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@":
                rpos = (x, y)
                # remove robot
                grid[y][x] = "."
                break

    print(rpos)

    # do the operations
    for op in ops:
        dir = op2Dir(op)
        nr_boxes = 0
        canMove = False
        npos = rpos
        # first follow direction forward
        while True:
            npos = (npos[0] + dir[0], npos[1] + dir[1])
            # check if pos is occupied
            vpos = grid[npos[1]][npos[0]]
            if vpos == ".":
                # add end
                canMove = True
                break
            elif vpos == "O":
                nr_boxes += 1
            elif vpos == "#":
                break

        # then follow backwards
        if canMove:
            rDir = reverseDir(dir)
            if nr_boxes > 0:
                # if moving box the next spot should get a box
                grid[npos[1]][npos[0]] = "O"
                # the first spot should be the robot
                first_pos = (npos[0] + (rDir[0] * nr_boxes), npos[1] + (rDir[1] * nr_boxes))
            else:
                first_pos = npos
            grid[first_pos[1]][first_pos[0]] = "."  # make empty
            # move original robot
            if first_pos == (0, 0):
                print("error")
            rpos = first_pos

    # calculate gps
    sum_gps = 0
    for y, line in enumerate(grid):
        for x, v in enumerate(line):
            if v == "O":
                sum_gps += 100 * y + x
    print("Part 1 =", sum_gps)


def reverseDir(dir: Tuple[int, int]) -> Tuple[int, int]:
    if dir == (-1, 0):
        return (1, 0)
    elif dir == (1, 0):
        return (-1, 0)
    elif dir == (0, 1):
        return (0, -1)
    elif dir == (0, -1):
        return (0, 1)
    raise ValueError(f"Unknown dir {dir}")


def op2Dir(op: str) -> Tuple[int, int]:
    if op == "<":
        return (-1, 0)
    elif op == ">":
        return (1, 0)
    elif op == "^":
        return (0, -1)
    elif op == "v":
        return (0, 1)

    raise ValueError(f"unknown op {op}")


def print_grid(grid, rpos=None):
    if rpos is not None:
        copy_grid = copy.deepcopy(grid)
        copy_grid[rpos[1]][rpos[0]] = "@"
        grid = copy_grid

    for line in grid:
        print("".join(line))


def find_robot(grid):
    rpos = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@":
                rpos = (x, y)
                # remove robot
                grid[y][x] = "."
                break

    return rpos


def extend_grid(grid):
    ext_grid = []
    for y, row in enumerate(grid):
        ext_grid.append([])
        for v in row:
            if v == "O":
                ext_grid[y].extend(["[", "]"])
            elif v == "@":
                ext_grid[y].extend(["@", "."])
            else:
                ext_grid[y].append(v)
                ext_grid[y].append(v)

    return ext_grid


def operationLeftRight(grid, op, robot):
    assert op == "<" or op == ">"
    dir = op2Dir(op)
    nr_boxes = 0
    canMove = False
    npos = robot
    # first follow direction forward
    while True:
        npos = (npos[0] + dir[0], npos[1])
        # check if pos is occupied
        vpos = grid[npos[1]][npos[0]]
        if vpos == ".":
            # add end
            canMove = True
            break
        elif vpos == "[":
            nr_boxes += 2
        elif vpos == "#":
            break

    # then follow backwards
    if canMove:
        rDir = reverseDir(dir)
        for _ in range(nr_boxes + 1):
            prev_pos = (npos[0] + rDir[0], npos[1])
            # change npos to prev
            grid[npos[1]][npos[0]] = grid[prev_pos[1]][prev_pos[0]]
            npos = prev_pos

        robot = (robot[0] + dir[0], robot[1])
    return robot


def operationUpDown(grid, op, robot):
    assert op == "^" or op == "v"
    dir = op2Dir(op)
    canMove = True
    npos = robot
    # first follow direction forward
    encountered_boxes = []
    to_check = deque()
    to_check.append(robot)
    while len(to_check) > 0:
        npos = to_check.popleft()
        npos = (npos[0], npos[1] + dir[1])
        # check if pos is occupied
        vpos = grid[npos[1]][npos[0]]
        if vpos == ".":
            # add end
            continue
        elif vpos == "[":
            # new box
            other_side = (npos[0] + 1, npos[1])
            encountered_boxes.append((npos, other_side))
            to_check.append(npos)
            to_check.append(other_side)
        elif vpos == "]":
            # new box
            other_side = (npos[0] - 1, npos[1])
            encountered_boxes.append((other_side, npos))
            to_check.append(npos)
            to_check.append(other_side)
        elif vpos == "#":
            canMove = False
            break

    if canMove:
        # move every box, because boxes are in order of rows, can reverse it
        for box in reversed(encountered_boxes):
            lpos = (box[0][0], box[0][1] + dir[1])
            rpos = (box[1][0], box[1][1] + dir[1])
            # add new box
            grid[lpos[1]][lpos[0]] = "["
            grid[rpos[1]][rpos[0]] = "]"
            # remove old boxes
            grid[box[0][1]][box[0][0]] = "."
            grid[box[1][1]][box[1][0]] = "."

        robot = (robot[0], robot[1] + dir[1])
    return robot


def part2():
    grid, ops = load_input()
    grid = extend_grid(grid)

    robot = find_robot(grid)
    # remove robot
    grid[robot[1]][robot[0]] = "."

    # do the operations
    for op in ops:
        # print_grid(grid, robot)
        # print(f"move {op}")
        if op == "<" or op == ">":
            robot = operationLeftRight(grid, op, robot)
        else:
            robot = operationUpDown(grid, op, robot)

    # print_grid(grid, robot)
    # calculate gps
    sum_gps = 0
    for y, line in enumerate(grid):
        for x, v in enumerate(line):
            if v == "[":
                sum_gps += 100 * y + x
    print("Part 1 =", sum_gps)


def load_input():
    with open("inputs/15.txt") as fp:
        sequence = fp.read()
        left, operations = sequence.split("\n\n")
        operations = operations.replace("\n", "")
        grid = []
        for line in left.split("\n"):
            grid.append(list(line))

    return grid, operations


if __name__ == "__main__":
    main()
