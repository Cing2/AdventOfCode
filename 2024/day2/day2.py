import copy
from typing import List


def main():
    part1()
    part2()


def part1():
    reports = load_lines()

    count_safe = 0
    for report in reports:
        if report_safe(report):
            count_safe += 1

    print("Day 1")
    print("Part 1 = ", count_safe)


def report_safe(report: List[int]) -> bool:
    # check if report is safe, by only ascending or descending
    ascending = report[0] < report[1]
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if ascending:  # check a change in ascending or descending
            if diff < 0:
                return False
        else:
            if diff > 0:
                return False
        if 0 == abs(diff) or abs(diff) > 3:  # diff must be between 1 and 3 inclusive
            return False

    return True


def part2():
    reports = load_lines()

    count_safe = 0
    for report in reports:
        is_safe = report_safe(report)
        if is_safe:
            count_safe += 1
        else:
            # brute force every removal
            for i in range(len(report)):
                cp_report = copy.copy(report)
                del cp_report[i]
                if report_safe(cp_report):
                    count_safe += 1
                    break
    print("Part 2 = ", count_safe)


def load_lines():
    reports = []
    with open("inputs/2.txt") as fp:
        for line in fp.readlines():
            nums = line.strip().split(" ")
            values = [int(x) for x in nums]
            reports.append(values)

    return reports


if __name__ == "__main__":
    main()
