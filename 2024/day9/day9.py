from collections import defaultdict
import time


def main():
    print("Day 9")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print(f"Time taken =", t_part1 - t_start, "(s)")
    part2_new()
    t_end = time.perf_counter()
    print(f"Time taken =", t_end - t_part1, "(s)")


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
    sequence = [int(x) for x in sequence]
    # get mapping of size to files
    map_size_file = [[] for _ in range(9)]
    for i, v in enumerate(sequence):
        if i % 2 == 0:
            # file block
            length_file = int(v)
            id_file = i // 2
            map_size_file[length_file - 1].append((i, id_file))

    print(map_size_file)

    # contains the index of files that were move
    files_done = set()
    # calculate checksum in one go
    checksum = 0
    counter_full_file = 0
    for i, file_length in enumerate(sequence):
        # check if file was already moved, then skip
        if i in files_done:
            continue
        if i % 2 == 0:
            # length of file block
            id_file = i // 2
            for _ in range(file_length):
                # checksum is the index of current position in the extended file and the index(ID) in the compressed file
                print(f"Adding {counter_full_file} * {id_file}", counter_full_file * id_file)
                checksum += counter_full_file * id_file
                counter_full_file += 1
            # remove file from mapping
            for k, file in enumerate(map_size_file[file_length - 1]):
                if file[0] == i:
                    del map_size_file[file_length - 1][k]

        else:
            # length of blank space, find file(s) to move in space
            space_remaining = file_length
            while space_remaining > 0:
                for space in range(space_remaining, 0):
                    if len(map_size_file[space - 1]) > 0:  # check if file with this much space
                        file = map_size_file[space - 1].pop()
                        # check if not already used
                        if file[0] in files_done:
                            # skip
                            continue
                        files_done.add(file[0])
                        space_remaining -= space
                        # add count to checksum
                        for _ in range(space):
                            print(f"Adding {counter_full_file} * {file[1]}", counter_full_file * file[1])
                            checksum += counter_full_file * file[1]
                            counter_full_file += 1
                        # break loop, and search again if space remaining
                        break
                else:
                    # if loop ends normally no file found to move thus skipping
                    break

    print("Part 2 = ", checksum)


def part2_new():
    sequence = load_sequence()
    files = []
    for i, v in enumerate(sequence):
        if int(v) == 0:
            continue
        if i % 2 == 0:
            # id of file is i//2
            files.append([i // 2, int(v)])
        else:
            # -1 for empty space
            files.append([-1, int(v)])
    print(files)
    # iteratively move files
    idx_file = len(files) - 1
    while idx_file > 0:
        print(files[idx_file])
        if files[idx_file][0] == -1:
            print("skipping")
            idx_file -= 1
            continue

        for j in range(idx_file - 1):
            if files[j][0] == -1:
                # check if file can be moved
                if files[j][1] == files[idx_file][1]:
                    # same size substitute
                    move_file = files.pop(idx_file)
                    print(f"moving file {move_file} to {j}")
                    files[j][0] = move_file[0]
                    break
                elif files[j][1] > files[idx_file][1]:
                    # file moving is smaller
                    move_file = files.pop(idx_file)
                    print(f"moving file {move_file} to {j}")
                    files[j][1] -= move_file[1]
                    files.insert(j, move_file)
                    break
                    # idx_file +=1
        idx_file -= 1

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

    print(files)


def load_sequence():
    with open("samples/9.txt") as fp:
        sequence = fp.read()
    return sequence


if __name__ == "__main__":
    main()
