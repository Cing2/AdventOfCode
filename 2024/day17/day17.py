import math
import re
import time
from typing import List, Tuple


def main():
    print("Day 17")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def part1():
    registers, program = load_input()
    # print(registers, program)
    # for i in range(0, len(program), 2):
    #     print(program[i], program[i + 1])

    output = run_program(program, registers)
    print(",".join(map(str, output)))


def run_program(program, registers) -> str:
    inst_pointer = 0
    output = []
    max_loop = len(program)
    loop_count = 0
    while inst_pointer < len(program) - 1:

        # perform opcode and operand
        opcode = program[inst_pointer]
        operand = program[inst_pointer + 1]
        # get value of operand
        combo_op = 0
        if operand < 4:
            # literal operand
            combo_op = operand
        elif operand == 4:
            # register A
            combo_op = registers[0]
        elif operand == 5:
            # register B
            combo_op = registers[1]
        elif operand == 6:
            # register C
            combo_op = registers[2]
        else:
            raise ValueError("Unknown operand")

        if opcode == 0:
            # division of A / 2^combo
            registers[0] = int(registers[0] // (2**combo_op))
        elif opcode == 1:
            # B xor op
            registers[1] = int(registers[1] ^ operand)
        elif opcode == 2:
            # combo_op % 8
            registers[1] = combo_op % 8
        elif opcode == 3:
            # jump to operand if A >0
            if registers[0] > 0:
                inst_pointer = operand
                continue
        elif opcode == 4:
            # B xor C
            registers[1] ^= registers[2]
        elif opcode == 5:
            #  combo_op % 8 output
            output.append(combo_op % 8)
            # end loop if infinite
            loop_count += 1
            if loop_count > max_loop:
                break
        elif opcode == 6:
            # A / 2^combo to B
            registers[1] = registers[0] // (2**combo_op)
        elif opcode == 7:
            # A / 2^combo to c
            registers[2] = registers[0] // (2**combo_op)

        inst_pointer += 2

    return output


def binary_search_length(program: List[int], low: int, high: int, searchLower: bool = True) -> int:
    length_program = len(program)

    while low < high:
        mid = low + (high - low) // 2
        output = run_program(program, [mid, 0, 0])
        if searchLower:
            if len(output) == length_program:
                high = mid
            elif len(output) == length_program - 1:
                low = mid
        else:
            if len(output) == length_program:
                low = mid
            elif len(output) == length_program - 1:
                high = mid

        if (high - low) <= 1:
            break

    return high


def binary_search_bound(program: List[int], low: int, high: int, index_to_search: int, searchLower: bool = True) -> int:
    need_number = program[index_to_search]

    while low < high:
        mid = low + (high - low) // 2
        output = run_program(program, [mid, 0, 0])
        number_output = output[index_to_search]
        if searchLower:
            if number_output == need_number:
                high = mid
            else:
                low = mid
        else:
            if number_output == need_number:
                low = mid
            else:
                high = mid

        if (high - low) <= 1:
            break

    return high


def search_for_index_program(program: List[int], low: int, high: int, index_to_search: int) -> Tuple[int, int]:
    """Binary search program in range for output at index be same as program, outputs new range"""
    need_number = program[index_to_search]
    # print(f"search in {low, high}, at {index_to_search} for {need_number}")

    # range split into n regions, every region has a number, find bounds of that regions
    nr_regions = 12
    length_reg = (high - low) // nr_regions
    regions_number = []
    regions = [low + length_reg * i for i in range(nr_regions)]
    regions.append(high)
    index_needed_reg = -1
    for i, A in enumerate(regions):
        output = run_program(program, [A, 0, 0])
        regions_number.append(output[index_to_search])
        if output[index_to_search] == need_number and index_needed_reg == -1:
            index_needed_reg = i

    if index_needed_reg == -1:
        # raise ValueError("Could not find region")
        # print(f"could not find region, {index_to_search}")
        return []

    all_regions = []
    current_regions = []
    for i, v in enumerate(regions_number):
        if v != need_number:
            if len(current_regions) > 0:
                all_regions.append(current_regions)
                current_regions = []
        else:
            # in a region
            current_regions.append(i)

    region_bounds = []
    for reg in all_regions:
        # binary search bounds of the region
        new_bound = []
        new_bound.append(
            binary_search_bound(
                program,
                regions[max(min(reg) - 1, 0)],
                regions[min(reg)],
                index_to_search,
                searchLower=True,
            )
        )
        new_bound.append(
            binary_search_bound(
                program,
                regions[max(reg)],
                regions[min(max(reg) + 1, len(regions) - 1)],
                index_to_search,
                searchLower=False,
            )
        )
        region_bounds.append(new_bound)

    # print(f"Found regions {region_bounds}")

    return region_bounds


def part2():
    registers, program = load_input()
    # print(program)
    # find the range where the output is the same length as the program
    L = 2
    low = math.inf
    high = 0
    max_size = 0
    length_program = len(program)
    below = 0
    above = 0
    while max_size <= length_program:
        L = L * 2
        output = run_program(program, [L, 0, 0])
        if len(output) == length_program - 1:
            below = L
        if len(output) == length_program + 1:
            above = L
        if len(output) == length_program:
            low = min(L, low)
            high = max(high, L)
        max_size = max(len(output), max_size)
    # print(below, low, high, above)
    lowest = binary_search_length(program, below, low, searchLower=True)
    highest = binary_search_length(program, high, above, searchLower=False)
    print("searching over", lowest, highest, f"Diff: {highest-lowest}")

    bounds = find_all_bounds(program, [[lowest, highest]], index_to_search=len(program) - 1)
    # print(bounds)

    for A in range(bounds[0][0], bounds[0][1] + 1):
        output = run_program(program, [A, 0, 0])
        if program == output:
            print("found it", A)
            break


def find_all_bounds(program, bounds, index_to_search):
    if len(bounds) == 0:
        return

    for bound in bounds:
        if bound[1] - bound[0] < 500:
            return bounds
        new_bounds = search_for_index_program(program, bound[0], bound[1], index_to_search)

        newer = find_all_bounds(program, new_bounds, index_to_search - 1)
        if newer:
            return newer


def load_input():
    with open("inputs/17.txt") as fp:
        sequence = fp.read()
        registers = []
        left, right = sequence.split("\n\n")
        for line in left.split("\n"):
            registers.append(int(re.findall(r"\d+", line)[0]))
        program = [int(x) for x in right.strip("Program: ").split(",")]

    return registers, program


if __name__ == "__main__":
    main()
