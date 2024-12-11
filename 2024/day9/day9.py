import time


def main():
    print("Day 9")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print(f"Time taken =", t_part1 - t_start, "(s)")
    # part2()
    t_end = time.perf_counter()
    print(f"Time taken =", t_end - t_part1, "(s)")


def part1():
    sequence = load_sequence()
    # unwrap sequence to file blocks and space

    # fill in space with blocks from the back

    # calculate checksum

    # calculate checksum in one go
    checksum = 0
    counter_full_file = 0
    # keep track of the last file
    last_file_index = len(sequence) - 1
    last_file_ID = last_file_index // 2  # id is divided by 2 as each number in between is for whitespace
    last_file_remaining = int(sequence[last_file_index])
    for i, value in enumerate(sequence):
        if i >= last_file_index:
            # already done all files
            if last_file_remaining > 0:
                for _ in range(last_file_remaining):
                    # print(f"Adding {counter_full_file} * {last_file_ID}", counter_full_file * last_file_ID)
                    checksum += counter_full_file * last_file_ID
                    counter_full_file += 1

            break
        if i % 2 == 0:
            # length of file block
            id_file = i // 2
            for _ in range(int(value)):
                # checksum is the index of current position in the extended file and the index(ID) in the compressed file
                # print(f"Adding {counter_full_file} * {id_file}", counter_full_file * id_file)
                checksum += counter_full_file * id_file
                counter_full_file += 1
        else:
            # length of blank space
            for _ in range(int(value)):
                # get values from the back
                if last_file_remaining == 0:
                    # get new last file
                    last_file_index -= 2
                    # id is divided by 2 as each number in between is for whitespace
                    last_file_ID = last_file_index // 2
                    last_file_remaining = int(sequence[last_file_index])
                # print(f"Adding {counter_full_file} * {last_file_ID}", counter_full_file * last_file_ID)
                checksum += counter_full_file * last_file_ID
                last_file_remaining -= 1
                counter_full_file += 1

    print("Part 1 = ", checksum)


def part2():
    sequence = load_sequence()


def load_sequence():
    with open("inputs/9.txt") as fp:
        sequence = fp.read()
    return sequence


if __name__ == "__main__":
    main()
