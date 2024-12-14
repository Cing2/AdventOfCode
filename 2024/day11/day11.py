from collections import defaultdict
import time
from typing import List


def main():
    print("Day 11")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def part1():
    nums = load_input()
    # keep track of numbers with dictionary, thus not calculation the same number multiple times
    num_dict = defaultdict(lambda: 0)
    for num in nums:
        num_dict[num] += 1

    for _ in range(25):
        # apply rules
        next_num_dict = defaultdict(lambda: 0)
        for num, count in num_dict.items():
            if num == 0:
                # rule 1, 0 => 1
                next_num_dict[1] += count
            else:
                # rule 2, split even length number
                str_num = str(num)
                len_num = len(str_num)
                if num > 9 and len_num % 2 == 0:
                    num_left = int(str_num[: (len_num // 2)])
                    num_right = int(str_num[(len_num // 2) :])
                    next_num_dict[num_left] += count
                    next_num_dict[num_right] += count
                else:
                    # rule 3, multiply by 2024
                    next_num_dict[num * 2024] += count
        num_dict = next_num_dict

    # count nums
    count_nums = 0
    for _, c in num_dict.items():
        count_nums += c
    print("Part 1 =", count_nums)


def part2():
    nums = load_input()
    # keep track of numbers with dictionary, thus not calculation the same number multiple times
    num_dict = defaultdict(lambda: 0)
    for num in nums:
        num_dict[num] += 1

    for _ in range(75):
        # apply rules
        next_num_dict = defaultdict(lambda: 0)
        for num, count in num_dict.items():
            if num == 0:
                # rule 1, 0 => 1
                next_num_dict[1] += count
            else:
                # rule 2, split even length number
                str_num = str(num)
                len_num = len(str_num)
                if num > 9 and len_num % 2 == 0:
                    num_left = int(str_num[: (len_num // 2)])
                    num_right = int(str_num[(len_num // 2) :])
                    next_num_dict[num_left] += count
                    next_num_dict[num_right] += count
                else:
                    # rule 3, multiply by 2024
                    next_num_dict[num * 2024] += count
        num_dict = next_num_dict

    # count nums
    count_nums = 0
    for _, c in num_dict.items():
        count_nums += c
    print("Part 2 =", count_nums)


def load_input():
    with open("inputs/11.txt") as fp:
        sequence = fp.read()
        nums = [int(x) for x in sequence.strip().split(" ")]
    return nums


if __name__ == "__main__":
    main()
