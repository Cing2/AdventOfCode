from collections import deque, namedtuple
from enum import Enum, IntEnum
import heapq
import math
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

    # alpha star search
    cost = a_star_part1(start, DIR.RIGHT, end, grid)
    print("Part 1 =", cost)


class DIR(IntEnum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3


class Node:
    def __init__(self, position, dir, parent=None, g=0, h=0):
        self.position = position  # (x, y) position
        self.dir = dir
        self.parents = [parent] if parent is not None else None  # Parent node
        self.g = g  # Cost from start node
        self.h = h  # Heuristic cost to goal
        self.f = g + h  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f"Pos: {self.position}, {self.dir}, g={self.g}, h={self.h}, f={self.f}"


def a_star_part1(start, dir, goal, grid):
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

        for neighbor in get_neighbors(current_node, grid, goal, no_parents=True):
            # if a node with the same position as successor is in the closed list which has a
            # lower f than successor, skip this successor
            if (neighbor.position, neighbor.dir) in closed_list:
                if closed_list[(neighbor.position, neighbor.dir)] <= neighbor.g:
                    continue

            # if a node with the same position as  successor  is in the open list which has
            #   a lower g than successor, skip this successor otherwise, add  the node to the open list
            in_open = False
            for node in open_list:
                if node.position == neighbor.position and node.dir == neighbor.dir:
                    if node.g <= neighbor.g:
                        # skip this neighbor
                        in_open = True
                        break

            if not in_open:
                heapq.heappush(open_list, neighbor)

    return 0


CheapNode = namedtuple("cheapNode", "x, y, dir, cost")


def bfs_part2(start, dir, goal, grid):
    queue: deque[Node] = deque()
    visited = [[[[math.inf, []] for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # from, position
    queue.append((None, CheapNode(start[0], start[1], dir, 0)))

    lowest_cost_end = math.inf

    while len(queue) > 0:
        from_n, node = queue.popleft()

        # keep track of cheapest visit
        visited_node = visited[node.y][node.x][node.dir]
        if visited_node[0] > node.cost:
            visited_node[0] = node.cost
            if from_n is not None:
                visited_node[1] = [from_n]
            # only continue this node if first add position
        elif visited_node[0] == node.cost:
            visited_node[1].append(from_n)
            continue
        else:
            continue

        if node.x == goal[0] and node.y == goal[1]:
            # reached end
            lowest_cost_end = min(lowest_cost_end, node.cost)
            continue

        for neighbor in get_cheap_neigh(node, grid):
            if neighbor.cost < lowest_cost_end:
                queue.append((node, neighbor))

    # track back from all end directions
    all_pos = set()
    following = list()
    all_pos.add(goal)
    # get all froms at end
    for cost, froms in visited[goal[1]][goal[0]]:
        if cost == lowest_cost_end:
            for node in froms:
                following.append(node)
    # follow the froms
    while len(following) > 0:
        node = following.pop()
        all_pos.add((node.x, node.y))
        cost, froms = visited[node.y][node.x][node.dir]
        for n in froms:
            following.append(n)
    
    return len(all_pos)
        


def get_cheap_neigh(node, grid):
    neigbors: List[CheapNode] = []
    # turn left and right
    neigbors.append(CheapNode(node.x, node.y, turnAntiClock(node.dir), node.cost + 1000))
    neigbors.append(CheapNode(node.x, node.y, turnClockWise(node.dir), node.cost + 1000))
    # move forward
    new_pos = moveForward((node.x, node.y), node.dir)
    if pos_in_grid(new_pos[0], new_pos[1], len(grid), len(grid[0])) and grid[new_pos[1]][new_pos[0]] != "#":
        neigbors.append(CheapNode(new_pos[0], new_pos[1], node.dir, node.cost + 1))

    return neigbors


def a_star_part2(start, dir, goal, grid):
    # A* Pathfinding Algorithm
    open_list: List[Node] = []  # Priority queue for open nodes
    closed_list = dict()  # Set for closed nodes
    # nodes that reached the end in lowest g
    shortest_paths: List[Node] = []
    length_shortest = math.inf

    # Create the starting node and add it to the open list
    start_node = Node(start, dir, parent=None, g=0, h=heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)
        # print(current_node)
        if current_node.position == goal:
            # part 2 needs all shortest paths
            if len(shortest_paths) == 0:
                shortest_paths.append(current_node)
                length_shortest = current_node.g
            else:
                if current_node.g == length_shortest:
                    shortest_paths.append(current_node)
            continue

        # Add the current node to the closed list
        closed_list[(current_node.position, current_node.dir)] = current_node

        for neighbor in get_neighbors(current_node, grid, goal, no_parents=True):
            if neighbor.f > length_shortest:
                # skip because already have shorter path
                continue
            # if a node with the same position as successor is in the closed list which has a
            # lower f than successor, skip this successor
            if (neighbor.position, neighbor.dir) in closed_list:
                if closed_list[(neighbor.position, neighbor.dir)].g < neighbor.g:
                    continue
                # if closed_list[(neighbor.position, neighbor.dir)].g == neighbor.g:
                #     if neighbor.parents is not None:
                #         closed_list[(neighbor.position, neighbor.dir)].parents.extend(neighbor.parents)
                #     continue

            # if a node with the same position as  successor  is in the open list which has
            #   a lower g than successor, skip this successor otherwise, add  the node to the open list
            in_open = False
            for node in open_list:
                if node.position == neighbor.position and node.dir == neighbor.dir:
                    if node.g < neighbor.g:
                        # skip this neighbor
                        in_open = True
                        break
                    # elif node.g == neighbor.g:
                    #     # came to same node with different path
                    #     if neighbor.parents is not None:
                    #         node.parents.extend(neighbor.parents)
                    #     in_open = True
                    #     break

            if not in_open:
                heapq.heappush(open_list, neighbor)

    # print(shortest_paths)
    # calculate nr of nodes in all paths
    all_pos = set()
    for node in shortest_paths:
        to_follow = [node]
        while len(to_follow) > 0:
            next = to_follow.pop()
            all_pos.add(next.position)
            if next.parents is not None:
                for parent in next.parents:
                    to_follow.append(parent)

    return len(all_pos)


def heuristic(pos: Tuple[int, int], goal: Tuple[int, int]) -> int:
    # Heuristic function (Manhattan distance)
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
def get_neighbors(node: Node, grid: List[List[str]], goal: Tuple[int, int], no_parents=True):
    neighbors: List[Node] = []
    # turn 90 clockwise or anti clockwise
    neighbors.append(
        Node(
            node.position,
            dir=turnClockWise(node.dir),
            parent=node if not no_parents else None,
            g=node.g + 1000,
            h=node.h,
        )
    )
    neighbors.append(
        Node(
            node.position,
            dir=turnAntiClock(node.dir),
            parent=node if not no_parents else None,
            g=node.g + 1000,
            h=node.h,
        )
    )
    # move forward
    new_position = moveForward(node.position, node.dir)
    if (
        pos_in_grid(new_position[0], new_position[1], len(grid), len(grid[0]))
        and grid[new_position[1]][new_position[0]] != "#"
    ):
        neighbors.append(Node(new_position, dir=node.dir, parent=node if not no_parents else None, g=node.g + 1))
        neighbors[-1].h = heuristic(neighbors[-1].position, goal)

    return neighbors


def pos_in_grid(x: int, y: int, height: int, width: int) -> bool:
    return 0 <= x < width and 0 <= y < height


def part2():
    grid = load_input()
    start, end = find_start_end(grid)

    # alpha star search, get all shortest paths
    cost = bfs_part2(start, DIR.RIGHT, end, grid)
    print("Part 2 =", cost)


def load_input():
    with open("inputs/16.txt") as fp:
        grid = []
        for line in fp.readlines():
            grid.append(list(line.strip()))
    return grid


if __name__ == "__main__":
    main()
