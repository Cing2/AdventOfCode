import re


def main():
    part1()
    part2()


def part1():
    sequence = load_sequence()

    # search file for exact sequence mul(<d>,<d>)
    muls = re.findall("mul\([0-9]+,[0-9]+\)", sequence)
    # print(muls)
    # sum up multiples
    sum = 0
    for mul in muls:
        values = mul.strip("mul()").split(",")
        sum += int(values[0]) * int(values[1])

    print("Day 3")
    print("Part 1 = ", sum)


def part2():
    sequence = load_sequence()

    # search file for exact sequence mul(<d>,<d>)
    muls = re.findall("(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))", sequence)
    # sum up multiples
    sum = 0
    do = True
    for mul in muls:
        if mul[1] != "":
            do = True
        if mul[2] != "":
            do = False
        if mul[0] != "" and do:
            values = mul[0].strip("mul()").split(",")
            sum += int(values[0]) * int(values[1])

    print("Part 2 = ", sum)


def load_sequence():
    with open("inputs/3.txt") as fp:
        sequence = fp.read()
    return sequence


if __name__ == "__main__":
    main()
