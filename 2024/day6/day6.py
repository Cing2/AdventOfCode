import copy
from enum import Enum
from typing import Union


def main():
    print("Day 6")
    part1()
    part2()


class DIR(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3


def part1():
    grid = load_input()
    guard_dir, guard_pos = get_guard_start(grid)
    pos_visited = get_pos_visited(grid, guard_dir, guard_pos)

    print("Part 1 =", len(pos_visited))


def get_guard_start(grid) -> Union[tuple[int], DIR]:
    # get start pos
    guard_pos = 0
    guard_dir = -1
    for y, line in enumerate(grid):
        if isinstance(guard_dir, DIR):
            break
        for x, place in enumerate(line):
            if place != "." and place != "#":
                guard_pos = (x, y)
                # found guard
                if place == ">":
                    guard_dir = DIR.RIGHT
                elif place == "<":
                    guard_dir = DIR.LEFT
                elif place == "^":
                    guard_dir = DIR.UP
                elif place == "v":
                    guard_dir = DIR.DOWN
                break

    return guard_pos, guard_dir


def get_pos_visited(grid, guard_pos: tuple[int], guard_dir: DIR):
    height = len(grid)
    width = len(grid[0])

    # print(guard_pos, guard_dir)
    # follow guard path
    pos_visited = {guard_pos}
    while True:
        # get next_pos
        next_pos = get_next_pos(guard_pos, guard_dir)
        if not pos_in_grid(next_pos[0], next_pos[1], height, width):
            # gone of map stop
            break
        # check value of square
        if grid[next_pos[1]][next_pos[0]] == "#":
            # box turn right
            guard_dir = turn_right(guard_dir)
        else:
            # point, move guard
            guard_pos = next_pos
            pos_visited.add(guard_pos)

    return pos_visited


def pos_in_grid(x: int, y: int, height: int, width: int) -> bool:
    return 0 <= x < width and 0 <= y < height


def turn_right(dir: DIR) -> DIR:
    if dir == DIR.RIGHT:
        return DIR.DOWN
    elif dir == DIR.LEFT:
        return DIR.UP
    elif dir == DIR.DOWN:
        return DIR.LEFT
    elif dir == DIR.UP:
        return DIR.RIGHT
    return DIR.RIGHT


def get_next_pos(pos: tuple[int], dir: DIR) -> tuple[int]:
    if dir == DIR.RIGHT:
        return (pos[0] + 1, pos[1])
    elif dir == DIR.LEFT:
        return (pos[0] - 1, pos[1])
    elif dir == DIR.DOWN:
        return (pos[0], pos[1] + 1)
    elif dir == DIR.UP:
        return (pos[0], pos[1] - 1)
    return (0, 0)


def check_for_loop(grid, guard_pos, guard_dir):
    height = len(grid)
    width = len(grid[0])

    # follow guard path
    pos_visited = {(guard_pos, guard_dir)}
    turn_count = 0
    while True:
        # get next_pos
        next_pos = get_next_pos(guard_pos, guard_dir)
        if not pos_in_grid(next_pos[0], next_pos[1], height, width):
            # gone of map stop
            return False
        # check value of square
        if grid[next_pos[1]][next_pos[0]] == "#":
            # box turn right
            guard_dir = turn_right(guard_dir)
            turn_count += 1
        else:
            # point, move guard
            guard_pos = next_pos
            # small optimization, as a loop you need at least 4 turns
            if turn_count > 3:
                if (guard_pos, guard_dir) in pos_visited:
                    return True
            pos_visited.add((guard_pos, guard_dir))


def part2():
    grid = load_input()
    guard_pos, guard_dir = get_guard_start(grid)
    pos_visited = get_pos_visited(grid, guard_pos, guard_dir)

    # for every position visited, except start, check if blocking causes a loop
    pos_visited.remove(guard_pos)

    # change string to list of grid
    new_grid = []
    for line in grid:
        new_grid.append(list(line))
    grid = new_grid

    count_loops = 0
    for pos in pos_visited:
        # add a block to guard
        grid[pos[1]][pos[0]] = "#"

        # simulate to check for a loop
        if check_for_loop(new_grid, guard_pos, guard_dir):
            count_loops += 1

        # change grid back to original
        grid[pos[1]][pos[0]] = "."

    print("Part 2 =", count_loops)


def load_input():
    with open("inputs/6.txt") as fp:
        grid = []
        for line in fp.readlines():
            grid.append(line.strip())
    return grid


if __name__ == "__main__":
    main()
