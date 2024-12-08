import re


def main():
    part1()
    part2()


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
                for dir in DIRECTIONS:
                    next_pos = (x, y)
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
                                break
                            next_letter += 1
                        else:
                            # xmas not found
                            break

    print("Part 1 =", count_xmas)


def pos_in_grid(x: int, y: int, height: int, width: int) -> bool:
    return not (0 <= x < width and 0 <= y < height)


def part2():
    sequence = load_sequence()
    height = len(sequence)
    width = len(sequence[0])
    count_mas = 0

    # go over every position
    MAS = "MAS"
    for y in range(height):
        for x in range(width):
            if x == 0 or y == 0 or x == width - 1 or y == height - 1:
                continue
            # check if value is x
            if sequence[y][x] == "A":
                # do search for MAS cross
                left_up = sequence[y - 1][x - 1]
                left_down = sequence[y + 1][x - 1]
                right_up = sequence[y - 1][x + 1]
                right_down = sequence[y + 1][x + 1]

                if (left_up == "M" and right_down == "S") or (left_up == "S" and right_down == "M"):
                    if (left_down == "M" and right_up == "S") or (left_down == "S" and right_up == "M"):
                        # found mas cross
                        count_mas += 1

    print("Part 2 =", count_mas)


def load_sequence():
    with open("inputs/4.txt") as fp:
        sequence = []
        for lin in fp.readlines():
            sequence.append(lin.strip())

    return sequence


if __name__ == "__main__":
    main()
