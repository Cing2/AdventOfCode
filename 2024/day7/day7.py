import itertools
import time


def main():
    print("Day 7")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print(f"Time taken = {t_part1-t_start}(s)")
    part2()
    t_end = time.perf_counter()
    print(f"Time taken = {t_end-t_part1}(s)")


def part1():
    eques = load_sequence()
    # print(eques)

    # for equation check if possible to create
    total_possible = 0
    for eq in eques:
        # check recursively for every combination of + and * if possible
        for combi in itertools.product((0, 1), repeat=(len(eq[1]) - 1)):
            # calculate sum
            sum = eq[1][0]
            for i, option in enumerate(combi):
                if option == 0:
                    sum *= eq[1][i + 1]
                else:
                    sum += eq[1][i + 1]
            if sum == eq[0]:
                # equation possible
                total_possible += eq[0]
                break

    print("Part 1 =", total_possible)


def part2():
    eques = load_sequence()

    # for equation check if possible to create
    total_possible = 0
    for eq in eques:
        # check recursively for every combination of + and * if possible
        for combi in itertools.product((0, 1, 2), repeat=(len(eq[1]) - 1)):
            # calculate sum
            sum = eq[1][0]
            for i, option in enumerate(combi):
                if option == 0:
                    sum *= eq[1][i + 1]
                elif option == 2:
                    sum = int(str(sum) + str(eq[1][i + 1]))
                else:
                    sum += eq[1][i + 1]

                # early break if sum is more
                if sum > eq[0]:
                    break
            if sum == eq[0]:
                # equation possible
                total_possible += eq[0]
                break

    print("Part 1 =", total_possible)


def load_sequence():
    with open("inputs/7.txt") as fp:
        eques = []
        for line in fp.readlines():
            total, values = line.strip().split(": ")
            total = int(total)
            values = values.split(" ")
            for i, v in enumerate(values):
                values[i] = int(v)

            eques.append((total, values))

    return eques


if __name__ == "__main__":
    main()
