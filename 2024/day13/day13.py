import time
import numpy as np


def main():
    print("Day 13")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    # part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def part1():
    claw_machines = load_input()
    # print(claw_machines)

    tokens = 0
    for machine in claw_machines:
        answer = machine.solve()
        # check if both are round
        if np.all(np.isclose(answer, answer.astype(int), 0.00001)):
            print("found solution")
            print(answer)
            tokens += int(answer[0]) * 3 + int(answer[1]) * 1

    print("Part 1 =", tokens)


def part2():
    sequence = load_input()


class ClawMachine:
    A = []
    B = []
    prize = []

    def __repr__(self):
        return f"Buttons A={self.A}, B={self.B} and Prize={self.prize}"

    def get_numpy(self):
        return np.array([self.A, self.B]), np.array(self.prize)

    def solve(self):
        X, y = self.get_numpy()
        return np.linalg.solve(X.T, y)


def load_input():
    with open("samples/13.txt") as fp:
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
