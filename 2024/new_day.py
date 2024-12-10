import argparse
import os


default_py_file = """
def main():
    print("Day {day}")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print(f"Time taken = {t_part1-t_start}(s)")
    # part2()
    t_end = time.perf_counter()
    print(f"Time taken = {t_end-t_part1}(s)")


def part1():
    sequence = load_sequence()
    

def part2():
    sequence = load_sequence()


def load_sequence():
    with open("samples/{day}.txt") as fp:
        sequence = fp.read()
    return sequence


if __name__ == "__main__":
    main()
"""


def create_day(n: int):
    assert isinstance(n, int)
    name_day = f"day{n}"
    print(f"Creating {name_day}")

    if os.path.exists(name_day):
        print("day already created, skipping")
        return

    # create folder
    os.makedirs(name_day)
    # make python file
    path_file = f"{name_day}/day{n}.py"
    with open(path_file, "w") as fp:
        input_file = default_py_file.format(day=n)
        fp.write(input_file)
    # make input file
    with open(f"inputs/{n}.txt", "w") as fp:
        pass
    # make sample file
    with open(f"samples/{n}.txt", "w") as fp:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Create DAY", description="Create empty files for new day")
    parser.add_argument("day")
    args = parser.parse_args()

    create_day(int(args.day))
