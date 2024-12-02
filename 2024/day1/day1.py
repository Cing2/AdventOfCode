def main():
    part1()
    part2()


def part1():
    # load lines
    left, right = load_lines()
    # sort both lists
    left.sort()
    right.sort()

    # compute sum diff
    sum = 0
    for i in range(len(left)):
        sum += abs(left[i] - right[i])

    print("Day 1")
    print("Part 1 = ", sum)


def part2():
    # load lines
    left, right = load_lines()
    # sort both lists
    left.sort()
    right.sort()

    # compute similarity score
    sum = 0
    for num1 in left:
        # check how often in right number
        count = 0
        for num2 in right:
            if num2 == num1:
                count += 1
            if num2 > num1:
                break
        sum += num1 * count

    print("Part 1 = ", sum)


def load_lines():
    left, right = [], []
    with open("inputs/1.txt") as fp:
        for line in fp.readlines():
            x = line.strip().split(" ")
            a, b = -1, -1
            a = int(x[0])
            b = int(x[3])
            left.append(a)
            right.append(b)

    return left, right


if __name__ == "__main__":
    main()
