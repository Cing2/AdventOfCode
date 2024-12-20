import time
from typing import Tuple


def main():
    print("Day 15")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    # part2()
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


def part2():
    sequence = load_input()


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
