package day12

import (
	"aoc/2023/common"
	"fmt"
	"strings"
)

func calcCombinations(row string, sets *[]int) int {
	// calculate how many combinations are possible that are correct
	var indexQ = strings.Index(row, "?")
	if indexQ == -1 {
		// all filled check if row is possible with set
		var nextArrang = 0
		var countHash = 0
		for _, c := range row {
			if c == '#' {
				// continue counting
				countHash += 1
			} else if countHash > 0 {
				// check if value is in set
				if countHash == (*sets)[nextArrang] {
					nextArrang += 1
				} else {
					// to many # for next one
					return 0
				}
				countHash = 0
			}
		}
		if countHash > 0 {
			if countHash == (*sets)[nextArrang] {
				nextArrang += 1
			}
		}
		if len(*sets) == nextArrang {
			// sets are the same
			return 1
		}
		return 0
	} else {
		// recurse over solutions
		var new0 = strings.Replace(row, "?", "#", 1)
		var new1 = strings.Replace(row, "?", ".", 1)

		return calcCombinations(new0, sets) + calcCombinations(new1, sets)
	}
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	var sum = 0
	for scanner.Scan() {
		splits := strings.Split(scanner.Text(), " ")
		var row = splits[0]
		var sets = common.StringToInts(&splits[1], ",")
		combies := calcCombinations(row, &sets)
		fmt.Println(combies)
		sum += combies

	}

	return sum
}

func Part2(filename string) int {
	// scanner, f := common.FileBuffer(filename)
	// defer f.Close()

	return 0
}
