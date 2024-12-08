from collections import defaultdict
import re
from typing import Dict, List


def main():
    print("Day 5")
    part1()
    part2()


def parse_rules(rules: List[int]) -> Dict[int, int]:
    rules_dict = defaultdict(list)
    for rule in rules:
        rules_dict[rule[0]].append(rule[1])

    return rules_dict


def part1():
    rules, updates = load_sequence()
    rules = parse_rules(rules)
    # print(rules, updates)

    sum_updates = 0

    for update in updates:
        update_in_order = True
        # check if update is in correct order
        for i in range(0, len(update) - 1):
            if not update_in_order:
                break
            for j in range(i + 1, len(update)):
                if update[i] in rules[update[j]]:
                    # print(f"update {update} not in order, because {update[i]}, {update[j]}")
                    update_in_order = False
                    break

        if update_in_order:
            sum_updates += update[len(update) // 2]

    print("Part 1 =", sum_updates)


def part2():
    rules, updates = load_sequence()
    rules = parse_rules(rules)
    # print(rules, updates)

    sum_updates = 0

    for update in updates:
        update_in_order = True
        # check if update is in correct order
        for i in range(0, len(update) - 1):
            for j in range(i + 1, len(update)):
                if update[i] in rules[update[j]]:
                    # print(f"update {update} not in order, because {update[i]}, {update[j]}")
                    update_in_order = False
                    # swap numbers
                    # print(f"swapping, {update[i]}, {update[j]}")
                    update[i], update[j] = update[j], update[i]

        if not update_in_order:
            sum_updates += update[len(update) // 2]

    print("Part 1 =", sum_updates)


def load_sequence():
    with open("inputs/5.txt") as fp:
        rules = []
        updates = []
        check_rules = True
        for line in fp.readlines():
            # print(line, check_rules)
            if line.strip() == "":
                check_rules = False
                continue
            if check_rules:
                # parse rules
                values = line.strip().split("|")
                rules.append((int(values[0]), int(values[1])))
            else:
                # parse updates

                values = line.strip().split(",")
                ints = []
                for v in values:
                    ints.append(int(v))
                updates.append(ints)

    return rules, updates


if __name__ == "__main__":
    main()
