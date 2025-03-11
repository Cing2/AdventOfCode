from collections import defaultdict, deque, namedtuple
import math
import time
from typing import List


def main():
    print("Day 20")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    new_part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def find_start_end(grid):
    start = (0, 0)
    end = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start = Position(x, y)
            elif grid[y][x] == "E":
                end = Position(x, y)

    return start, end


Position = namedtuple("Postion", "x y")
Dim = namedtuple("Dim", "pos id_cheater")
Node = namedtuple("Node", "dim cost")


class Counter:
    def __init__(self, start: int):
        self.value = start

    def next_value(self) -> int:
        self.value += 1
        return self.value


def manhatten_dist(pos: Position, end: Position) -> int:
    return abs(pos.x - end.x) + abs(pos.y - end.y)


def distance_to_end(grid, end: Position) -> dict[Position, int]:
    # do bfs from end to get distance from each node
    queue = deque()
    visited = set()
    start = Node(Dim(end, 0), 0)
    queue.append(start)
    visited.add(start.dim.pos)
    dist_to_end = {}

    while len(queue) > 0:
        node = queue.popleft()

        dist_to_end[node.dim.pos] = node.cost

        for neigh in get_neighbors(node, grid, None):
            if neigh.dim.pos in visited:
                continue

            queue.append(neigh)
            visited.add(neigh.dim.pos)

    # print(sorted(list(dist_to_end.items()), key=lambda x: x[1]))
    return dist_to_end


def part1():
    grid = load_input(test=False)
    start, end = find_start_end(grid)
    dist_to_end = distance_to_end(grid, end)

    # bfs over grid with cheat option
    visited = set()
    queue = deque()
    start = Node(Dim(Position(start[0], start[1]), 0), 0)
    queue.append(start)
    visited.add(start)
    cheater = deque()
    counter_ids = Counter(0)
    finished_cheaters = []
    min_dist_end = math.inf

    while len(queue) > 0 or len(cheater) > 0:
        if len(queue) > 0:
            node = queue.popleft()
        else:
            node = cheater.popleft()

        if node.dim.id_cheater > 0 and node.dim.pos in dist_to_end:
            # use known distance to calculate cost for cheater
            new_node = Node(
                Dim(Position(0, 0), 0), node.cost + dist_to_end[node.dim.pos]
            )
            finished_cheaters.append(new_node)
            continue

        if node.dim.pos == end:
            # at end
            if node.dim.id_cheater == 0:
                min_dist_end = node.cost

        # get all neighbors
        for neigh in get_neighbors(node, grid, counter_ids):
            if neigh.dim in visited:
                continue

            if neigh.dim.id_cheater > 0:
                cheater.append(neigh)
            else:
                queue.append(neigh)

            visited.add(neigh.dim)

    count_100_save = 0
    for cheater in finished_cheaters:
        diff = min_dist_end - cheater.cost
        if diff >= 100:
            count_100_save += 1

    print("Part 1 =", count_100_save)


def get_neighbors(
    node: Node, grid, counter_ids: Counter, cheat_amount: int = 1
) -> List[Node]:
    neigbors = []
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dir in dirs:
        new_pos = Position(node.dim.pos.x + dir[0], node.dim.pos.y + dir[1])
        if pos_in_grid(new_pos[0], new_pos[1], len(grid), len(grid[0])):
            if isinstance(node, Cheater):
                if grid[new_pos[1]][new_pos[0]] != "#" or node.rem_steps > 0:
                    is_prev_block = grid[node.dim.pos.x][node.dim.pos.y] == "#"
                    neigbors.append(
                        Cheater(
                            Dim(new_pos, node.dim.id_cheater),
                            node.cost + 1,
                            node.start_pos,
                            is_prev_block,
                            node.rem_steps - 1,
                        )
                    )
            else:
                if grid[new_pos[1]][new_pos[0]] != "#":
                    neigbors.append(
                        Node(Dim(new_pos, node.dim.id_cheater), node.cost + 1)
                    )
                else:
                    if (
                        node.dim.id_cheater == 0 and counter_ids is not None
                    ):  # not cheating, new cheater
                        id_cheater = counter_ids.next_value()
                        neigbors.append(
                            Cheater(
                                Dim(new_pos, id_cheater),
                                node.cost + 1,
                                node.dim.pos,
                                False,
                                cheat_amount,
                            )
                        )

    return neigbors


def pos_in_grid(x: int, y: int, height: int, width: int) -> bool:
    return 0 <= x < width and 0 <= y < height


Cheater = namedtuple("Cheater", "dim cost start_pos prev_block rem_steps")


def new_part2(test=False):
    grid = load_input(test)
    start, end = find_start_end(grid)
    dist_to_end = distance_to_end(grid, end)
    dist_to_start = distance_to_end(grid, start)

    allowed_cheat = 20
    min_save = 100
    if test:
        min_save = 50

    min_normal_dist = dist_to_end[start]

    # possible_cheats = dict()
    count_cheats = 0
    # for every combination of two positions
    for pos1, distS1 in dist_to_start.items():
        # # skip position if not possible to save enough
        # abs_dist_end = abs(pos1.x - end.x) + abs(pos1.y - end.y)
        # max_savings = min_normal_dist - (distS1 + abs_dist_end)
        # if max_savings < min_save:
        #     continue
        for pos2, distE2 in dist_to_end.items():
            if pos1 == pos2:
                continue  # skip same position
            # check if possible to cheat between, and check if cheat saves anything
            dist = abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)
            if dist <= allowed_cheat:
                # cost is dist to 1 then dist to 2 and then from 2 to end
                cost = distS1 + dist + distE2
                savings = min_normal_dist - cost
                if savings >= min_save:
                    count_cheats += 1
                    # possible_cheats[(pos1, pos2)] = savings

    # print(possible_cheats)
    # count_saved = defaultdict(lambda: 0)
    # for _, savings in possible_cheats.items():
    #     count_saved[savings] += 1
    # print(sorted(list(count_saved.items())))

    print("Part 2 =", count_cheats)


def load_input(test):
    file = "inputs/20.txt"
    if test:
        file = "samples/20.txt"
    with open(file) as fp:
        grid = []
        for line in fp.readlines():
            grid.append(line.strip())
    return grid


if __name__ == "__main__":
    main()
