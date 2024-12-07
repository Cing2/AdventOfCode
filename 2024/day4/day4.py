import re


def main():
    part1()
    # part2()


def part1():
    sequence = load_sequence()

    height = len(sequence)
    width = len(sequence[0])

    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    count_xmas = 0

    # go over every position
    MAS = "MAS"
    for y in range(height):
        for x in range(width):
            # check if value is x
            if sequence[y][x] == "X":
                # do search for xmas in every direction
                next_pos = (x, y)
                for dir in DIRECTIONS:
                    next_letter = 0
                    while True:
                        next_pos = (next_pos[0] + dir[0], next_pos[1] + dir[1])
                        # check pos on grid
                        if not (0 <= next_pos[0] < width and 0 <= next_pos[1] < height):
                            break
                        if sequence[next_pos[1]][next_pos[0]] == MAS[next_letter]:
                            # found new letter
                            if next_letter >= 2:
                                # full xmas
                                count_xmas += 1
                                print(x, y, dir)
                                break
                            next_letter += 1
                        else:
                            # xmas not found
                            break

    print("Part 1 =", count_xmas)


def part2():
    sequence = load_sequence()


def load_sequence():
    with open("samples/4.txt") as fp:
        sequence = []
        for lin in fp.readlines():
            sequence.append(lin.strip())

    return sequence


if __name__ == "__main__":
    main()
