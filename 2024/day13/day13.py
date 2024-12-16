import time
import numpy as np


def main():
    print("Day 13")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def part1():
    claw_machines = load_input()

    tokens = 0
    for machine in claw_machines:
        # check if linear independent
        if machine.get_rank() < 2:
            print("Not full", machine)

        answer = machine.solve()
        tokens += answer

    print("Part 1 =", tokens)


def part2():
    claw_machines = load_input()

    tokens = 0
    for machine in claw_machines:
        # check if linear independent
        if machine.get_rank() < 2:
            print("Not full", machine)

        answer = machine.solve(add=np.array([10000000000000, 10000000000000]))
        tokens += answer

    print("Part 2 =", tokens)


class ClawMachine:
    A = []
    B = []
    prize = []

    def __repr__(self):
        return f"Buttons A={self.A}, B={self.B} and Prize={self.prize}"

    def get_numpy(self):
        return np.array([self.A, self.B]), np.array(self.prize)

    def get_rank(self):
        X, y = self.get_numpy()
        return np.linalg.matrix_rank(X)

    def solve(self, add=np.array([0, 0])):
        X, y = self.get_numpy()
        y = y + add
        answer = np.linalg.solve(X.T, y)
        answer = answer.round()
        if (X.T @ answer == y).all():
            return int((answer @ [3, 1]).sum())
        return 0


def load_input():
    with open("inputs/13.txt") as fp:
        claw_machines = []
        new_machine = ClawMachine()
        for line in fp.readlines():
            if line.startswith("Button"):
                left, right = line.strip().split(",")
                x = int(left[(left.index("+") + 1) :])
                y = int(right[(right.index("+") + 1) :])
                if "A" in line:
                    new_machine.A = [x, y]
                elif "B" in line:
                    new_machine.B = [x, y]

            if line.startswith("Prize"):
                left, right = line.strip().split(",")
                x = int(left[(left.index("=") + 1) :])
                y = int(right[(right.index("=") + 1) :])
                new_machine.prize = [x, y]

            if line.strip() == "":
                claw_machines.append(new_machine)
                new_machine = ClawMachine()

        if len(new_machine.A) > 0:
            claw_machines.append(new_machine)
            new_machine = ClawMachine()

    return claw_machines


if __name__ == "__main__":
    main()
