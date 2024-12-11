from collections import defaultdict, namedtuple
import itertools
import time


def main():
    print("Day 8")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print(f"Time taken = {t_part1-t_start}(s)")
    part2()
    t_end = time.perf_counter()
    print(f"Time taken = {t_end-t_part1}(s)")


def part1():
    ant_sets, size_grid = load_input()
    print(ant_sets, size_grid)

    distortion_points = set()
    for _, ants in ant_sets.items():
        for combi in itertools.combinations(ants, r=2):
            print(combi)
            # get all distortion points
            # a+ (a-b) = 2a-b
            dist = (2 * combi[0][0] - combi[1][0], 2 * combi[0][1] - combi[1][1])
            # check if point on grid
            if pos_in_grid(dist[0], dist[1], size_grid.height, size_grid.width):
                distortion_points.add(dist)
            # b - (a-b) = 2b-a
            dist = (2 * combi[1][0] - combi[0][0], 2 * combi[1][1] - combi[0][1])
            if pos_in_grid(dist[0], dist[1], size_grid.height, size_grid.width):
                distortion_points.add(dist)

    print("Part 1 =", len(distortion_points))


def pos_in_grid(x: int, y: int, height: int, width: int) -> bool:
    return 0 <= x < width and 0 <= y < height


def part2():
    ant_sets, size_grid = load_input()
    print(ant_sets, size_grid)

    distortion_points = set()
    for _, ants in ant_sets.items():
        for combi in itertools.combinations(ants, r=2):
            print(combi)
            # get all distortion points
            # a+ (a-b) = 2a-b
            dist = (2 * combi[0][0] - combi[1][0], 2 * combi[0][1] - combi[1][1])
            # check if point on grid
            if pos_in_grid(dist[0], dist[1], size_grid.height, size_grid.width):
                distortion_points.add(dist)
            # b - (a-b) = 2b-a
            dist = (2 * combi[1][0] - combi[0][0], 2 * combi[1][1] - combi[0][1])
            if pos_in_grid(dist[0], dist[1], size_grid.height, size_grid.width):
                distortion_points.add(dist)

    print("Part 1 =", len(distortion_points))


Size = namedtuple("size", ("width", "height"))


def load_input():
    with open("inputs/8.txt") as fp:
        antennas = defaultdict(list)
        grid = []
        for y, line in enumerate(fp.readlines()):
            line = line.strip()
            grid.append(line)
            for x, char in enumerate(line):
                if char != ".":
                    antennas[char].append((x, y))

        size = Size(len(grid[0]), len(grid))
    return antennas, size


if __name__ == "__main__":
    main()
