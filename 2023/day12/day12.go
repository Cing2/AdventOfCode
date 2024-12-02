package day12

import (
	"aoc/2023/common"
	"strings"
)

type combination struct {
	curV      byte
	nextSet   int
	countHash int
	rem_row   string
}

func calcCombinationsCached(row *string, sets *[]int, curI int, curV byte, nextSet int, countHash int, cache *map[combination]int) int {
	// recusively check every character of the string at the time
	// check if cache contains combinations
	combie, ok := (*cache)[combination{curV, nextSet, countHash, (*row)[curI:]}]
	if ok {
		return combie
	}

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
		combies := calcCombinationsCached(row, sets, curI, '#', nextSet, countHash, cache) + calcCombinationsCached(row, sets, curI, '.', nextSet, countHash, cache)
		(*cache)[combination{curV, nextSet, countHash, (*row)[(curI):]}] = combies
		return combies
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
		combies := calcCombinationsCached(row, sets, curI+1, (*row)[curI+1], nextSet, countHash, cache)
		(*cache)[combination{curV, nextSet, countHash, (*row)[(curI + 1):]}] = combies
		return combies
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
		var cache = map[combination]int{}
		combies := calcCombinationsCached(&row, &sets, 0, row[0], 0, 0, &cache)

		sum += combies
	}

	return sum
}

// Assumption: n >= 0
func IntPow(base, exp int) int {
	result := 1
	for {
		if exp&1 == 1 {
			result *= base
		}
		exp >>= 1
		if exp == 0 {
			break
		}
		base *= base
	}

	return result
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
		var newSets []int
		var moreRows []string
		for i := 0; i < 5; i++ {
			newSets = append(newSets, sets...)
			moreRows = append(moreRows, row)
		}
		var newRow = strings.Join(moreRows, "?")

		var cache = map[combination]int{}
		combies := calcCombinationsCached(&newRow, &newSets, 0, newRow[0], 0, 0, &cache)

		sum += combies
	}

	return sum
}
