package day3

import (
	"aoc/2023/common"
	"bufio"
	"fmt"
	"strconv"
	"unicode"
)

type Number struct {
	value     int
	positions []Pos
}
type Pos struct {
	x int
	y int
}

func extractNumbers(scanner *bufio.Scanner) ([]string, []Number) {
	var lines []string
	var numbers []Number
	var i = 0
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
		// get numbers
		var currentNum = ""
		var positions []Pos
		for j, char := range scanner.Text() {
			if unicode.IsDigit(char) {
				currentNum += string(char)
				positions = append(positions, Pos{i, j})
			} else if len(currentNum) > 0 {
				// save number
				var num, _ = strconv.Atoi(currentNum)
				var newNum = Number{num, positions}
				numbers = append(numbers, newNum)
				currentNum = ""
				positions = []Pos{}
			}

		}
		if len(currentNum) > 0 {
			// save number
			var num, _ = strconv.Atoi(currentNum)
			var newNum = Number{num, positions}
			numbers = append(numbers, newNum)
			currentNum = ""
		}

		i += 1
	}
	return lines, numbers
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	lines, numbers := extractNumbers(scanner)

	var sum = 0
	// for every number check if they are attached to an object
	for _, num := range numbers {
		var attached = false
		for _, pos := range num.positions {
			if attached {
				break
			}
			// for every index arround it check if position has a object
			for i := -1; i < 2; i++ {
				for j := -1; j < 2; j++ {
					var newPos = Pos{pos.x + i, pos.y + j}
					// check if position is in range numbers
					if 0 <= newPos.x && newPos.x < len(lines) && 0 <= newPos.y && newPos.y < len(lines[0]) {
						if !unicode.IsDigit(rune(lines[newPos.x][newPos.y])) && lines[newPos.x][newPos.y] != '.' {
							// found surrouning object
							attached = true
							break
						}
					}
				}
			}
		}
		if attached {
			sum += num.value
		}
	}
	fmt.Printf("Sum = %d\n", sum)

	return sum
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	lines, numbers := extractNumbers(scanner)

	var gears = make(map[Pos][]int)
	// for every number check if they are attached to an object
	for _, num := range numbers {
		var attached = false
		for _, pos := range num.positions {
			if attached {
				break
			}
			// for every index arround it check if position has a object
			for i := -1; i < 2; i++ {
				if attached {
					break
				}
				for j := -1; j < 2; j++ {
					var newPos = Pos{pos.x + i, pos.y + j}
					// check if position is in range numbers
					if 0 <= newPos.x && newPos.x < len(lines) && 0 <= newPos.y && newPos.y < len(lines[0]) {
						if !unicode.IsDigit(rune(lines[newPos.x][newPos.y])) && lines[newPos.x][newPos.y] == '*' {
							// found surrouning gear
							if gears[newPos] == nil {
								gears[newPos] = []int{num.value}
							} else {
								gears[newPos] = append(gears[newPos], num.value)
							}
							attached = true
							break
						}
					}
				}
			}
		}
	}

	var sum = 0
	for _, nums := range gears{
		if len(nums) >1{
			// get multiple and add to sum
			var ratio = 1
			for _, num := range nums {
				ratio = ratio*num
			}
			sum += ratio
		}

	}

	fmt.Printf("Sum = %d\n", sum)
	return sum
}
