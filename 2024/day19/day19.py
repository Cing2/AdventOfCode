from functools import cache
import time
from typing import List


def main():
    print("Day 19")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def part1():
    towels, patterns = load_input()
    # print(towels, patterns)

    count = 0
    for pat in patterns:
        # check if pattern can be made
        if make_pattern(pat, towels):
            count += 1
    print("Part 1 = ", count)


def make_pattern(pattern: str, towels: List[str]) -> bool:
    # base case
    if pattern == "":
        return True

    # get all towels that fit start of pattern
    fitted = []
    for towel in towels:
        if pattern.startswith(towel):
            fitted.append(towel)

    # recursively check if pattern can be made with pattern
    for fit in fitted:
        if make_pattern(pattern[len(fit) :], towels):
            return True

    return False


def part2():
    towels, patterns = load_input()
    # print(towels, patterns)

    @cache
    def count_pattern(pattern: str) -> int:
        # base case
        if pattern == "":
            return 1

        # get all towels that fit start of pattern
        fitted = []
        for towel in towels:
            if pattern.startswith(towel):
                fitted.append(towel)

        # recursively check if pattern can be made with pattern
        count = 0
        for fit in fitted:
            count += count_pattern(pattern[len(fit) :])

        return count

    count = 0
    for pat in patterns:
        # check if pattern can be made
        pat_c = count_pattern(pat)
        count += pat_c
    print("Part 2 = ", count)


def load_input():
    with open("inputs/19.txt") as fp:
        sequence = fp.read()
        left, right = sequence.split("\n\n")
        towels = [x.strip() for x in left.strip().split(",")]
        patterns = right.split("\n")
    return towels, patterns


if __name__ == "__main__":
    main()
