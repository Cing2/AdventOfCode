package day5

import (
	"aoc/2023/common"
	"bufio"
	"fmt"
	"slices"
	"strings"
)

type mapping struct {
	// from string
	// to string
	ranges []ranges
}

type ranges struct {
	dest   int
	source int
	length   int
}

func parseInput(scanner *bufio.Scanner) ([]int, []mapping){
	var i = 0
	var seeds []int
	var maps []mapping
	var newMapping mapping

	for scanner.Scan() {
		i += 1
		if i == 1 {
			// get seeds
			splits := strings.Split(scanner.Text(), ":")
			seeds = common.StringToInts(&splits[1])
			continue
		}
		var text = scanner.Text()
		if text == "" {
			//skip blank line
			continue
		}
		if strings.Contains(text, "map") {
			if len(newMapping.ranges) > 0 {
				maps = append(maps, newMapping)
			}
			newMapping = mapping{}
			continue
		}
		// else it is a range
		var numbers = common.StringToInts(&text)
		newMapping.ranges = append(newMapping.ranges, ranges{numbers[0], numbers[1], numbers[2]})
	}

	maps = append(maps, newMapping)
	// fmt.Println(maps)

	return seeds, maps
}

func checkIntinRange(num int, rang *ranges) int{
	dif := num - rang.source
	if dif >= 0 && dif < rang.length {
		// num in range
		return dif
	}
	return -1
}
func processSeeds(seeds *[]int,  *[]mapping) {

	var results []int
	for _, seed := range seeds {
		// follow seed trhough maps
		for _, mapping := range maps {
			for _, ranges := range mapping.ranges {
				// check if seed in range 
				if dif :=checkIntinRange(seed, &ranges); dif >=0 {
					// range fits convert seed
					seed = ranges.dest + dif
					break
				}
			}
		}
		results = append(results, seed)
	}
	return slices.Min(results)
}


func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	seeds, maps := parseInput(scanner)

	// fmt.Println(results)

	fmt.Println("Answer: ", slices.Min(results))

	return slices.Min(results)
}

func Part2(filename string) int {

	return 0
}
