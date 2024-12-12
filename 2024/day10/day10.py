from collections import deque
import time


def main():
    print("Day 10")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print(f"Time taken =", t_part1 - t_start, "(s)")
    part2()
    t_end = time.perf_counter()
    print(f"Time taken =", t_end - t_part1, "(s)")


def part1():
    grid = load_input()

    height = len(grid)
    width = len(grid[0])
    # get all trail heads
    trail_heads = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 0:
                trail_heads.append((x, y))

    sum_heads = 0
    for head in trail_heads:
        # do dfs to get score
        queue = deque()
        queue.append(head)
        visited = set()
        head_paths = 0
        while len(queue) > 0:
            npos = queue.popleft()
            # print(npos)
            if npos in visited:
                continue
            visited.add(npos)
            pos_value = grid[npos[1]][npos[0]]
            if pos_value == 9:
                head_paths += 1
            # get neighbours
            neighbours = [
                (npos[0] - 1, npos[1]),
                (npos[0] + 1, npos[1]),
                (npos[0], npos[1] - 1),
                (npos[0], npos[1] + 1),
            ]
            for neigh in neighbours:
                if pos_in_grid(neigh[0], neigh[1], height, width):
                    neigh_value = grid[neigh[1]][neigh[0]]
                    if neigh_value == pos_value + 1:
                        if neigh in visited:
                            # skip
                            break
                        queue.append(neigh)
        # print(head_paths)
        sum_heads += head_paths

    print("Part 1 =", sum_heads)


def pos_in_grid(x: int, y: int, height: int, width: int) -> bool:
    return 0 <= x < width and 0 <= y < height


def part2():
    grid = load_input()

    height = len(grid)
    width = len(grid[0])
    # get all trail heads
    trail_heads = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 0:
                trail_heads.append((x, y))

    sum_heads = 0
    for head in trail_heads:
        # do dfs to get score
        queue = deque()
        queue.append(head)
        visited = set()
        head_paths = 0
        while len(queue) > 0:
            npos = queue.popleft()
            # print(npos)
            # if npos in visited:
            #     continue
            # visited.add(npos)
            pos_value = grid[npos[1]][npos[0]]
            if pos_value == 9:
                head_paths += 1
            # get neighbours
            neighbours = [
                (npos[0] - 1, npos[1]),
                (npos[0] + 1, npos[1]),
                (npos[0], npos[1] - 1),
                (npos[0], npos[1] + 1),
            ]
            for neigh in neighbours:
                if pos_in_grid(neigh[0], neigh[1], height, width):
                    neigh_value = grid[neigh[1]][neigh[0]]
                    if neigh_value == pos_value + 1:
                        # if neigh in visited:
                        #     # skip
                        #     break
                        queue.append(neigh)
        # print(head_paths)
        sum_heads += head_paths

    print("Part 2 =", sum_heads)


def load_input():
    with open("inputs/10.txt") as fp:
        grid = []
        for line in fp.readlines():
            grid.append([int(x) for x in list(line.strip())])
    return grid


if __name__ == "__main__":
    main()
