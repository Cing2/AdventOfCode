import time

def main():
    print("Day 9")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print(f"Time taken =", t_part1-t_start, "(s)")
    # part2()
    t_end = time.perf_counter()
    print(f"Time taken =", t_end-t_part1, "(s)")
    

def part1():
    sequence = load_sequence()
    

def part2():
    sequence = load_sequence()


def load_sequence():
    with open("samples/9.txt") as fp:
        sequence = fp.read()
    return sequence


if __name__ == "__main__":
    main()
