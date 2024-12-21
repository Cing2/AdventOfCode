import re
import time


def main():
    print("Day 17")
    t_start = time.perf_counter()
    part1()
    t_part1 = time.perf_counter()
    print("Time taken =", t_part1 - t_start, "(s)")
    # part2()
    t_end = time.perf_counter()
    print("Time taken =", t_end - t_part1, "(s)")


def part1():
    registers, program = load_input()
    print(registers, program)
    inst_pointer = 0
    for i in range(0, len(program), 2):
        print(program[i], program[i+1])

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
            registers[0] = registers[0] // 2**combo_op
        elif opcode == 1:
            # B xor op
            registers[1] ^= operand
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
            print(combo_op % 8, end=",")
        elif opcode == 6:
            # A / 2^combo to B
            registers[1] = registers[0] // 2**combo_op
        elif opcode == 7:
            # A / 2^combo to c
            registers[2] = registers[0] // 2**combo_op

        inst_pointer += 2
    print("")


def part2():
    registers, program = load_input()
    # reverse program to get the same output
    next_output = len(program)-1
    need_registers = [None, None, None]

    



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
