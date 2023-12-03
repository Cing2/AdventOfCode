package day1

import (
	"aoc/2023/common"
	"fmt"
	"strconv"
	"unicode"
)

func Part1(filename string) int {
	scanner := common.FileBuffer(filename)

	var sum int = 0

	for scanner.Scan() {
		// get al integers from string
		var numbers []rune
		for _, c := range scanner.Text() {
			if unicode.IsDigit(c) {
				numbers = append(numbers, c)
			}
		}

		// combine first and last charcter number to int
		num, _ := strconv.Atoi(string(numbers[0]) + string(numbers[len(numbers)-1]))
		sum += num
	}

	fmt.Printf("Sum = %d", sum)
	return sum
}

func Part2(filename string) int {
	scanner := common.FileBuffer(filename)

	var sum int = 0

	for scanner.Scan() {
		// loop over line and retrieve numbers

		
	}

	return sum
}
