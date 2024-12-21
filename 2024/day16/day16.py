from enum import Enum
import heapq
import time
from typing import List, Tuple


def main():
    print("Day 16")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def find_start_end(grid):
    start = (0, 0)
    end = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start = (x, y)
            elif grid[y][x] == "E":
                end = (x, y)

    return start, end


def part1():
    grid = load_input()
    start, end = find_start_end(grid)
    print(start, end)

    # alpha star search
    cost = a_star(start, DIR.RIGHT, end, grid)
    print("Part 1 =", cost)


class DIR(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3


class Node:
    def __init__(self, position, dir, parent=None, g=0, h=0):
        self.position = position  # (x, y) position
        self.dir = dir
        self.parent = parent  # Parent node
        self.g = g  # Cost from start node
        self.h = h  # Heuristic cost to goal
        self.f = g + h  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f"Pos: {self.position}, {self.dir}, g={self.g}, h={self.h}, f={self.f}"


def a_star(start, dir, goal, grid):
    # A* Pathfinding Algorithm
    open_list: List[Node] = []  # Priority queue for open nodes
    closed_list = dict()  # Set for closed nodes

    # Create the starting node and add it to the open list
    start_node = Node(start, dir, parent=None, g=0, h=heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)
        # print(current_node)

        # If we've reached the goal, return the cost
        if current_node.position == goal:
            return current_node.g

        # Add the current node to the closed list
        closed_list[(current_node.position, current_node.dir)] = current_node.g

        # Check neighbors (8 directions for a grid)
        for neighbor in get_neighbors(current_node, grid, goal):
            # if a node with the same position as successor is in the OPEN list which has a
            # lower f than successor, skip this successor
            if (neighbor.position, neighbor.dir) in closed_list and closed_list[
                (current_node.position, current_node.dir)
            ] <= neighbor.g:
                continue

            # if a node with the same position as  successor  is in the CLOSED list which has
            #   a lower f than successor, skip this successor otherwise, add  the node to the open list
            in_open = False
            for node in open_list:
                if node.position == neighbor.position and node.dir == neighbor.dir and node.g < neighbor.g:
                    # skip this neighbor
                    in_open = True
                    break

            if not in_open:
                heapq.heappush(open_list, neighbor)

    return 0


# Heuristic function (Manhattan distance)
def heuristic(pos: Tuple[int, int], goal: Tuple[int, int]):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


def turnClockWise(dir: DIR) -> DIR:
    if dir == DIR.RIGHT:
        return DIR.DOWN
    elif dir == DIR.LEFT:
        return DIR.UP
    elif dir == DIR.DOWN:
        return DIR.LEFT
    elif dir == DIR.UP:
        return DIR.RIGHT
    return DIR.RIGHT


def turnAntiClock(dir: DIR) -> DIR:
    if dir == DIR.RIGHT:
        return DIR.UP
    elif dir == DIR.LEFT:
        return DIR.DOWN
    elif dir == DIR.DOWN:
        return DIR.RIGHT
    elif dir == DIR.UP:
        return DIR.LEFT
    return DIR.RIGHT


def moveForward(pos: Tuple[int, int], dir: DIR) -> Tuple[int, int]:
    if dir == DIR.RIGHT:
        return (pos[0] + 1, pos[1])
    elif dir == DIR.LEFT:
        return (pos[0] - 1, pos[1])
    elif dir == DIR.DOWN:
        return (pos[0], pos[1] + 1)
    elif dir == DIR.UP:
        return (pos[0], pos[1] - 1)


def print_grid(grid):
    for line in grid:
        print("".join(line))


# Get valid neighbors of a node in the grid
def get_neighbors(node: Node, grid: List[List[str]], goal: Tuple[int, int]):
    neighbors: List[Node] = []
    # turn 90 clockwise or anti clockwise
    neighbors.append(Node(node.position, dir=turnClockWise(node.dir), g=node.g + 1000, h=node.h))
    neighbors.append(Node(node.position, dir=turnAntiClock(node.dir), g=node.g + 1000, h=node.h))
    # move forward
    new_position = moveForward(node.position, node.dir)
    if (
        pos_in_grid(new_position[0], new_position[1], len(grid), len(grid[0]))
        and grid[new_position[1]][new_position[0]] != "#"
    ):
        neighbors.append(Node(new_position, dir=node.dir, g=node.g + 1))
        neighbors[-1].h = heuristic(neighbors[-1].position, goal)

    return neighbors


def pos_in_grid(x: int, y: int, height: int, width: int) -> bool:
    return 0 <= x < width and 0 <= y < height


# Check if node is in the open list
def in_open_list(node, open_list):

    return any(n.position == node.position for n in open_list)


def part2():
    sequence = load_input()


def load_input():
    with open("inputs/16.txt") as fp:
        grid = []
        for line in fp.readlines():
            grid.append(list(line.strip()))
    return grid


if __name__ == "__main__":
    main()
