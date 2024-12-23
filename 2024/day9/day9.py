from collections import defaultdict
import time


def main():
    print("Day 9")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def part1():
    sequence = load_sequence()
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
    files = []
    for i, v in enumerate(sequence):
        if int(v) == 0:
            continue
        if i % 2 == 0:  # if uneven is a file
            # id of file is i//2
            files.append([i // 2, int(v), False])
        else:
            # -1 for empty space
            files.append([-1, int(v), False])

    # iteratively move files
    i = len(files) - 1
    while i > 0:
        # check if empty space or already moved
        if files[i][0] == -1 or files[i][2] == True:
            i -= 1
            continue

        for j in range(i):
            if files[j][0] == -1:
                # check if file can be moved
                if files[j][1] == files[i][1]:
                    # same size substitute
                    # change emtpy to file
                    files[j][0] = files[i][0]
                    files[j][2] = True  # indicate that files is already moved
                    # make file empty
                    files[i][0] = -1
                    break
                elif files[j][1] > files[i][1]:
                    # file moving is smaller
                    # reduce empty space
                    files[j][1] -= files[i][1]
                    # files[j][2] = True
                    # insert new file before
                    files.insert(j, [files[i][0], files[i][1], True])
                    i += 1
                    # change original file to empty
                    files[i][0] = -1
                    break

        i -= 1

    # calculate hash of combination
    idx_counter = 0
    checksum = 0
    for file in files:
        if file[0] == -1:
            idx_counter += file[1]
            continue
        for _ in range(file[1]):
            checksum += idx_counter * file[0]
            idx_counter += 1

    print("part 2 =", checksum)


def load_sequence():
    with open("inputs/9.txt") as fp:
        sequence = fp.read().strip()
    return sequence


if __name__ == "__main__":
    main()
