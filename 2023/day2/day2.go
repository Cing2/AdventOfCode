package day2

import (
	"aoc/2023/common"
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseInput(buffer *bufio.Scanner, f *os.File) {
	defer f.Close()

}

var maxCubes = map[string]int{
	"red":   12,
	"green": 13,
	"blue":  14,
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()

	var sum int = 0
	var index = 0
	for scanner.Scan() {
		index += 1
		var linePossible = true
		// check all inputs if it is possible
		var splits = strings.Split(scanner.Text(), ":")
		// split on ; per draw
		var draws = strings.Split(splits[1], ";")
		// per draw check if possible
		for _, draw := range draws {
			var cubes = strings.Split(draw, ",")
			for _, cube := range cubes {
				var ab = strings.Split(strings.Trim(cube, " "), " ")
				// fmt.Println(ab)
				var num, _ = strconv.Atoi(ab[0])
				if maxCubes[ab[1]] < num {
					linePossible = false
				}
			}
		}

		if linePossible {
			sum += index
		}

	}

	fmt.Printf("Sum = %d\n", sum)
	return sum
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()

	var sum int = 0
	for scanner.Scan() {
		var minColors = map[string]int{
			"red":   0,
			"green": 0,
			"blue":  0,
		}
		// check all inputs if it is possible
		var splits = strings.Split(scanner.Text(), ":")
		// split on ; per draw
		var draws = strings.Split(splits[1], ";")
		// per draw check if possible
		for _, draw := range draws {
			var cubes = strings.Split(draw, ",")
			for _, cube := range cubes {
				var ab = strings.Split(strings.Trim(cube, " "), " ")
				var num, _ = strconv.Atoi(ab[0])
				minColors[ab[1]] = max(minColors[ab[1]], num)
			}
		}

		// add the power of minimum cubes
		sum += minColors["red"] * minColors["green"] * minColors["blue"]
	}

	fmt.Printf("Sum = %d\n", sum)
	return sum
}
