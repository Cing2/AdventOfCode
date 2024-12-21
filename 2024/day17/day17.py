
import time

def main():
    print("Day 17")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1-t_start, "(s)")
    # part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end-t_part1, "(s)")
    

def part1():
    sequence = load_input()
    

def part2():
    sequence = load_input()


def load_input():
    with open("samples/17.txt") as fp:
        sequence = fp.read()
    return sequence


if __name__ == "__main__":
    main()
