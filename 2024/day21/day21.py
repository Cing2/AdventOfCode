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

#   0   1   2
# +---+---+---+
# | 7 | 8 | 9 | 0
# +---+---+---+
# | 4 | 5 | 6 | 1
# +---+---+---+
# | 1 | 2 | 3 | 2
# +---+---+---+
#     | 0 | A | 3
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
    "3": Point(2, 2),
    "0": Point(1, 3),
    "A": Point(2, 3),
}

direct_to_position = {
    "^": Point(1, 0),
    "A": Point(2, 0),
    "<": Point(0, 1),
    "v": Point(1, 1),
    ">": Point(2, 1),
}

pos_to_direct = {v: k for v, k in direct_to_position.items()}
pos_to_numeric = {v: k for v, k in direct_to_position.items()}


def move_keyboards(pos_on: Point, pos_to: Point) -> str:
    if pos_to == pos_on:
        return "A"
    # to right
    if pos_to.x > pos_on.x:
        return ">" + move_keyboards(Point(pos_on.x + 1, pos_on.y), pos_to)
    # going up
    if pos_to.y < pos_on.y:
        return "^" + move_keyboards(Point(pos_on.x, pos_on.y - 1), pos_to)
    # down
    if pos_to.y > pos_on.y:
        return "v" + move_keyboards(Point(pos_on.x, pos_on.y + 1), pos_to)
    # to left
    if pos_to.x < pos_on.x:
        return "<" + move_keyboards(Point(pos_on.x - 1, pos_on.y), pos_to)


def recurse_boards(values: str, boards: list) -> str:
    on_square = "A"
    sum_motion = ""
    keyboard = direct_to_position
    if not boards[0]:
        keyboard = numeric_position
    pos_on = keyboard[on_square]

    for value in values:
        pos_to = keyboard[value]
        motion = move_keyboards(pos_on, pos_to)
        print(f'{len(boards)} Working on ', motion)
        pos_on = keyboard[value]
        if len(boards) > 1:
            sum_motion += recurse_boards(motion, boards[1:])
        else:
            sum_motion += motion
    print(len(boards), values, sum_motion)

    return sum_motion


def part1():
    codes = load_input()
    boards = [False, True, True]

    sum = 0
    for code in codes[-1:]:
        answer = recurse_boards(code, [False, True, True])
        # number
        num = int(code.strip("A"))
        sum += num * len(answer)
        print(code, answer, len(answer), num)

    print("Part 1 =", sum)


def part2():
    sequence = load_input()


def load_input():
    with open("samples/21.txt") as fp:
        codes = [line.strip() for line in fp.readlines()]
    return codes


if __name__ == "__main__":
    main()
