from collections import namedtuple
from functools import cache
import time


def main():
    print("Day 21")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    # part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

Point = namedtuple("point", "x, y")
numeric_position = {
    "7": Point(0, 0),
    "8": Point(1, 0),
    "9": Point(2, 0),
    "4": Point(0, 1),
    "5": Point(1, 1),
    "6": Point(2, 1),
    "1": Point(0, 2),
    "2": Point(1, 2),
    "0": Point(1, 3),
    "8": Point(2, 3),
}

directional_position = {
    "^": Point(1, 0),
    "A": Point(2, 0),
    "<": Point(0, 1),
    "v": Point(1, 1),
    ">": Point(2, 1),
}


@cache
def numeric_keyboard(on: str, to: str) -> str:
    if to == on:
        return ""
    pos_on = numeric_position[on]
    pos_to = numeric_position[to]
    # going up
    if pos_to.y < pos_on.y:
        return "^" + numeric_keyboard(Point(pos_on.x, pos_on.y - 1), pos_to)
    # to right
    if pos_to.x > pos_on.x:
        return ">" + numeric_keyboard(Point(pos_on.x + 1, pos_on.y), pos_to)
    # to left
    if pos_to.x < pos_on.x:
        return "<" + numeric_keyboard(Point(pos_on.x - 1, pos_on.y), pos_to)
    # down
    if pos_to.y > pos_on.y:
        return "^" + numeric_keyboard(Point(pos_on.x, pos_on.y + 1), pos_to)


def part1():
    codes = load_input()


def part2():
    sequence = load_input()


def load_input():
    with open("samples/21.txt") as fp:
        codes = [line.strip() for line in fp.readlines()]
    return codes


if __name__ == "__main__":
    main()
