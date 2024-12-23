import math
import os
import re
import time

import numpy as np


def main():
    print("Day 14")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def part1():
    pos, vel = load_input()
    # over 100 steps
    size_room = np.array([101, 103])
    new = (pos + 100 * vel) % size_room
    # remove robots on middle line
    half_room = size_room // 2
    new = new[~(new == half_room).any(1)]
    # get quadrant of each robot
    quad = (new) // (half_room + np.array([1, 1]))
    quad = quad[:, 0] + 2 * quad[:, 1]
    _, counts = np.unique(quad, return_counts=True)
    sum = np.prod(counts)
    print("Part 1 =", sum)


def part2():
    pos, vel = load_input()
    size_room = np.array([101, 103])
    copy_pos = np.copy(pos)
    lowest_security_code = math.inf
    lowest_i = 0
    for i in range(10000):
        # move 1 step
        pos = (pos + vel) % size_room
        # calculate security code
        # remove robots on middle line
        half_room = size_room // 2
        new = pos[~(pos == half_room).any(1)]
        # get quadrant of each robot
        quad = (new) // (half_room + np.array([1, 1]))
        quad = quad[:, 0] + 2 * quad[:, 1]
        _, counts = np.unique(quad, return_counts=True)
        security_code = np.prod(counts)
        if security_code < lowest_security_code:
            lowest_security_code = security_code
            lowest_i = i

    # show robots at lowest security code
    pos = (copy_pos + (lowest_i + 1) * vel) % size_room
    print_grid(pos, size_room)
    print(f"lowest security code is {lowest_security_code} at iteration {lowest_i}")


def print_grid(pos, grid_size):
    unique_pos = np.unique(pos, axis=1)
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            if (unique_pos == np.array([x, y])).all(1).any():
                print("X", end="")
            else:
                print(".", end="")
        print("")


def load_input():
    with open("inputs/14.txt") as fp:
        sequence = fp.read()
        pos = []
        vel = []
        for line in sequence.split("\n"):
            x, y, v_x, v_y = map(int, re.findall(r"-?\d+", line))
            pos.append(np.array([x, y]))
            vel.append(np.array([v_x, v_y]))

        pos = np.array(pos)
        vel = np.array(vel)
    return pos, vel


if __name__ == "__main__":
    main()
