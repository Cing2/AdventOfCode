from collections import defaultdict, deque
import time


def main():
    print("Day 12")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def part1():
    grid = load_input()

    height = len(grid)
    width = len(grid[0])

    visited = set()
    sum_regions = 0

    id_region = 0
    for y in range(height):
        for x in range(width):
            if (x, y) in visited:
                continue  # skip pos
            id_region += 1
            # do dfs on area to calculate area and fence
            letter_area = grid[y][x]
            queue = deque()
            queue.append((x, y))
            area_region = 0
            fence_region = 0
            while len(queue) > 0:
                npos = queue.popleft()
                if npos in visited:
                    continue
                visited.add(npos)
                area_region += 1

                neighbours = [
                    (npos[0] - 1, npos[1]),
                    (npos[0] + 1, npos[1]),
                    (npos[0], npos[1] - 1),
                    (npos[0], npos[1] + 1),
                ]
                for neigh in neighbours:
                    if not pos_in_grid(neigh[0], neigh[1], height, width):
                        fence_region += 1
                        continue
                    if grid[neigh[1]][neigh[0]] == letter_area:
                        # add to next pos
                        if neigh not in visited:
                            queue.append(neigh)
                    else:
                        fence_region += 1

            sum_regions += area_region * fence_region

    print("Part 1 =", sum_regions)


def pos_in_grid(x: int, y: int, height: int, width: int) -> bool:
    return 0 <= x < width and 0 <= y < height


def part2():
    grid = load_input()

    height = len(grid)
    width = len(grid[0])

    visited = set()
    map_regions = {}
    id_region = 0
    regions = {}
    for y in range(height):
        for x in range(width):
            if (x, y) in visited:
                continue  # skip pos
            id_region += 1
            # do dfs on area to calculate area and fence
            letter_area = grid[y][x]
            queue = deque()
            queue.append((x, y))
            area_region = 0
            while len(queue) > 0:
                npos = queue.popleft()
                if npos in visited:
                    continue
                visited.add(npos)
                map_regions[npos] = id_region
                area_region += 1

                neighbours = [
                    (npos[0] - 1, npos[1]),
                    (npos[0] + 1, npos[1]),
                    (npos[0], npos[1] - 1),
                    (npos[0], npos[1] + 1),
                ]
                for neigh in neighbours:
                    if not pos_in_grid(neigh[0], neigh[1], height, width):
                        continue
                    if grid[neigh[1]][neigh[0]] == letter_area:
                        # add to next pos
                        if neigh not in visited:
                            queue.append(neigh)

            regions[id_region] = [letter_area, area_region, 0]

    # calculate fence area seperately
    # go over rows
    print_region_id = -1
    for y in range(height):
        prev_v = ""
        region_id = -1
        # if following a fence
        follow_up = False
        follow_down = False
        for x in range(width):
            value = grid[y][x]
            if value != prev_v:
                follow_down = False
                follow_up = False
                prev_v = value
                region_id = map_regions[(x, y)]

            # up has a fence if not on grid or not same value
            up_fence = (not pos_in_grid(x, y - 1, height, width)) or (grid[y - 1][x] != value)
            down_fence = (not pos_in_grid(x, y + 1, height, width)) or (grid[y + 1][x] != value)
            if up_fence:
                if not follow_up:
                    follow_up = True
                    regions[region_id][2] += 1
                    if region_id == print_region_id:
                        print((x, y), "U")
            else:
                follow_up = False
            if down_fence:
                if not follow_down:
                    follow_down = True
                    regions[region_id][2] += 1
                    if print_region_id == region_id:
                        print((x, y), "D")
            else:
                follow_down = False
    # go over columns
    for x in range(width):
        prev_v = ""
        region_id = -1
        # if following a fence
        follow_left = False
        follow_right = False
        for y in range(height):
            value = grid[y][x]
            if value != prev_v:
                follow_right = False
                follow_left = False
                prev_v = value
                region_id = map_regions[(x, y)]

            # up has a fence if not on grid or not same value
            left_fence = (not pos_in_grid(x - 1, y, height, width)) or (grid[y][x - 1] != value)
            right_fence = (not pos_in_grid(x + 1, y, height, width)) or (grid[y][x + 1] != value)
            if left_fence:
                if not follow_left:
                    follow_left = True
                    regions[region_id][2] += 1
                    if print_region_id == region_id:
                        print((x, y), "L")
            else:
                follow_left = False
            if right_fence:
                if not follow_right:
                    follow_right = True
                    regions[region_id][2] += 1
                    if print_region_id == region_id:
                        print((x, y), "R")
            else:
                follow_right = False
    # calculate cost regions
    sum_regions = 0
    for reg, values in regions.items():
        # print(reg, values)
        sum_regions += values[1] * values[2]

    print("Part 2 =", sum_regions)


def load_input():
    with open("inputs/12.txt") as fp:
        grid = []
        for line in fp.readlines():
            grid.append(line.strip())
    return grid


if __name__ == "__main__":
    main()
