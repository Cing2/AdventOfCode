from collections import namedtuple
import heapq
import time
from typing import List, Tuple

import numpy as np


def main():
    print("Day 18")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def make_grid(points: List[List[int]], grid_size: Tuple[int, int], nr_points: int) -> np.ndarray:
    grid = np.zeros(grid_size)
    for i in range(nr_points):
        point = points[i]
        grid[point[0], point[1]] = 1

    return grid


def part1(test=False):
    points = load_input(test)
    grid_size = (71, 71)
    nr_points = 1024
    if test:
        grid_size = (7, 7)
        nr_points = 12

    grid = make_grid(points, grid_size, nr_points)

    # A star
    shortest_path = alpha_star(grid, Position(0, 0), Position(grid_size[0] - 1, grid_size[1] - 1))
    print("Part 1 =", shortest_path)


Position = namedtuple("Position", "x, y")


class Node:
    def __init__(self, pos: Position, g=0, h=0):
        self.pos: Position = pos  # (x, y) position
        self.g: int = g  # Cost from start node
        self.h: int = h  # Heuristic cost to goal
        self.f: int = g + h  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f"Pos: {self.pos}, g={self.g}, h={self.h}, f={self.f}"


def heuristic(pos: Tuple[int, int], goal: Tuple[int, int]) -> int:
    # Heuristic function (Manhattan distance)
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


def get_neighbors(node: Node, grid: List[List[str]], goal: Tuple[int, int]):
    neighbors: List[Node] = []
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dir in dirs:
        new_pos = Position(node.pos.x + dir[0], node.pos.y + dir[1])
        if pos_in_grid(new_pos[0], new_pos[1], len(grid), len(grid[0])) and grid[new_pos[1]][new_pos[0]] != 1:
            neighbors.append(Node(new_pos, node.g + 1, h=heuristic(new_pos, goal)))

    return neighbors


def pos_in_grid(x: int, y: int, height: int, width: int) -> bool:
    return 0 <= x < width and 0 <= y < height


def alpha_star(grid, start: Position, goal: Position):
    # A* Pathfinding Algorithm
    open_list: List[Node] = []  # Priority queue for open nodes
    closed_list = dict()  # Set for closed nodes

    # Create the starting node and add it to the open list
    start_node = Node(start, g=0, h=heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)
        # print(current_node)

        # If we've reached the goal, return the cost
        if current_node.pos == goal:
            return current_node.g

        # Add the current node to the closed list
        closed_list[current_node.pos] = current_node.g

        for neighbor in get_neighbors(current_node, grid, goal):
            # if a node with the same position as successor is in the closed list which has a
            # lower g than successor, skip this successor
            if neighbor.pos in closed_list and closed_list[neighbor.pos] <= neighbor.g:
                continue

            # if a node with the same position as  successor  is in the open list which has
            #  a lower g than successor, skip this successor otherwise, add  the node to the open list
            in_open = False
            for node in open_list:
                if node.pos == neighbor.pos:
                    if node.g <= neighbor.g:
                        # skip this neighbor
                        in_open = True
                        break

            if not in_open:
                heapq.heappush(open_list, neighbor)

    return 0


def reset_grid(grid, points: List[List[int]], nr_points: int) -> np.ndarray:
    # make empty
    grid[:] = 0
    for point in points[: (nr_points + 1)]:
        grid[point[0]][point[1]] = 1


def part2(test=False):
    points = load_input(test)
    grid_size = (71, 71)
    nr_points = 1024
    if test:
        grid_size = (7, 7)
        nr_points = 12

    grid = make_grid(points, grid_size, nr_points)

    start = Position(0, 0)
    end = Position(grid_size[0] - 1, grid_size[0] - 1)

    # do binary search for first point that does not
    left = nr_points
    right = len(points)
    while right >= left:
        # make grid
        mid = (right - left) // 2 + left
        reset_grid(grid, points, mid)
        # check if still reachable
        steps = alpha_star(grid, start, end)
        if steps == 0:
            right = mid
        else:
            left = mid

        if right - left <= 1:
            # should have found it
            print(f"Part 2 = i: {right}, ", points[right])
            break


def load_input(test=False):
    file = "inputs/18.txt"
    if test:
        file = "samples/18.txt"
    with open(file) as fp:
        points = []
        for line in fp.readlines():
            points.append([int(x) for x in line.strip().split(",")])

    return points


if __name__ == "__main__":
    main()
