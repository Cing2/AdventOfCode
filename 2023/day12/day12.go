package day12

import (
	"aoc/2023/common"
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
				if nextArrang < len(*sets) && countHash == (*sets)[nextArrang] {
					nextArrang += 1
				} else {
					// to  # for next one
					return 0
				}
				countHash = 0
			}
		}
		if countHash > 0 {
			if nextArrang < len(*sets) && countHash == (*sets)[nextArrang] {
				nextArrang += 1
			} else {
				return 0
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

func calcCombinations3(row *string, sets *[]int, curI int, curV byte, nextSet int, countHash int) int {
	// recusively check every character of the string at the time
	// for every charcter check if still following set and for ? check both
	if curV == '#' {
		// continue counting
		countHash += 1
		if nextSet < len(*sets) && countHash > (*sets)[nextSet] {
			// stop when counting more hash then needed
			return 0
		}
	} else if curV == '.' {
		if countHash > 0 {
			// just close a hash set, check if value is in set
			if nextSet < len(*sets) && countHash == (*sets)[nextSet] {
				nextSet += 1
				countHash = 0
			} else {
				// either no more sets to complete or not right amount of <
				return 0
			}
		}
	} else if curV == '?' {
		// recurse on both options
		return calcCombinations3(row, sets, curI, '#', nextSet, countHash) + calcCombinations3(row, sets, curI, '.', nextSet, countHash)
	}

	// check if at end
	if curI == len(*row)-1 {
		// at end of row, final set check
		if countHash > 0 {
			if nextSet < len(*sets) && countHash == (*sets)[nextSet] {
				nextSet += 1
			} else {
				return 0
			}
		}
		// check if all sets satisfied
		if len(*sets) == nextSet {
			return 1
		}
		return 0
	} else {
		// go to next character
		return calcCombinations3(row, sets, curI+1, (*row)[curI+1], nextSet, countHash)
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
		combies := calcCombinations3(&row, &sets, 0, row[0], 0, 0)
		sum += combies
	}

	return sum
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()

	var sum = 0
	for scanner.Scan() {
		splits := strings.Split(scanner.Text(), " ")
		var row = splits[0]
		var sets = common.StringToInts(&splits[1], ",")
		// duplicate row 5 times
		row = strings.Join(row*5, "?")
		var newSet = 
		combies := calcCombinations3(&row, &sets, 0, row[0], 0, 0)
		sum += combies
	}

	return sum
}
