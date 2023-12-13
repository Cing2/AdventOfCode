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
	ranges []map_range
}

type map_range struct {
	dest   int
	source int
	length int
}

type arange struct {
	start  int
	length int
}

func parseInput(scanner *bufio.Scanner) ([]int, []mapping) {
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
		newMapping.ranges = append(newMapping.ranges, map_range{numbers[0], numbers[1], numbers[2]})
	}

	maps = append(maps, newMapping)
	// fmt.Println(maps)

	return seeds, maps
}

func checkIntinRange(num int, rang *map_range) int {
	dif := num - rang.source
	if dif >= 0 && dif < rang.length {
		// num in range
		return dif
	}
	return -1
}

func processSeeds(seeds *[]int, maps *[]mapping) int {
	var results []int
	for _, seed := range *seeds {
		// follow seed trhough maps
		for _, mapping := range *maps {
			for _, ranges := range mapping.ranges {
				// check if seed in range
				if dif := checkIntinRange(seed, &ranges); dif >= 0 {
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

	result := processSeeds(&seeds, &maps)
	fmt.Println("Answer: ", result)

	return result
}

func seedsInMap(seed *arange, mapping *map_range) ([]arange, []arange) {
	// check if ranges overlap
	diff := mapping.source - seed.start
	var remaining []arange
	var changed []arange

	if diff > 0 {
		// seed start is before map
		if diff < seed.length {
			// partial overlap seed start is before mapping
			// check if seed range is longer then whole mapping
			if seed.length > diff+mapping.length {
				// seed encompases range
				// remaining is same start and lenght upto start mapping
				// and start of end mapping and lenght minus diff and mapping length
				remaining = append(remaining, arange{seed.start, diff},
					arange{mapping.source + mapping.length, seed.length - diff - mapping.length})
				// seed is mapping destination and length minus diff
				changed = append(changed, arange{mapping.dest, mapping.length})
			}

			// remaining is same start and lenght upto start mapping
			remaining = append(remaining, arange{seed.start, diff})
			// seed is mapping destination and length minus diff
			changed = append(changed, arange{mapping.dest, seed.length - diff})
		} else {
			// no overlap
			remaining = append(remaining, *seed)
		}
	} else {
		// seed start is after or same as mapping start
		if common.AbsInt(diff) < mapping.length {
			// range overlap
			if seed.start+seed.length <= mapping.source+mapping.length {
				// fully contained
				// new seed is same length but with destination start
				changed = append(changed, arange{mapping.dest - diff, seed.length})

			} else {
				// partial overlap seed end is after mapping
				var lenghtInside = mapping.source + mapping.length - seed.start
				// remaining is start end of mapping and remaining length
				remaining = append(remaining, arange{mapping.source + mapping.length, seed.length - lenghtInside})
				// changed is destination + diff and length inside
				changed = append(changed, arange{mapping.dest + common.AbsInt(diff), lenghtInside})
			}
		} else {
			// no overlap seed if fully after range
			remaining = append(remaining, *seed)
		}
	}

	return remaining, changed
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	seeds, maps := parseInput(scanner)

	//expand ranges of seeds
	var seedRanges []arange
	for i, seed := range seeds {
		if i%2 == 0 {
			seedRanges = append(seedRanges, arange{seed, seeds[i+1]})
		}
	}

	var inputSeeds []arange = seedRanges
	var nextSeeds []arange
	var outputSeeds []arange

	for _, mapping := range maps {
		// follow seed through maps
		for _, ranges := range mapping.ranges {
			for _, seed := range inputSeeds {
				// check if seed range in map range
				remaining, changed := seedsInMap(&seed, &ranges)
				for _, rem := range remaining {
					// redo seed for next range
					nextSeeds = append(nextSeeds, rem)
				}
				for _, cha := range changed {
					// seed can go to next mapping
					outputSeeds = append(outputSeeds, cha)
				}
			}
			// swap input with next, as input is empty
			inputSeeds = nextSeeds
			nextSeeds = make([]arange, 0)
			if len(inputSeeds) == 0 {
				// already have all inputs done
				break
			}
		}
		// remaining seed remain the same
		for _, seed := range inputSeeds {
			outputSeeds = append(outputSeeds, seed)
		}
		// input should be empty and output should contain all seeds
		inputSeeds = outputSeeds
		outputSeeds = make([]arange, 0)
		if len(inputSeeds) > 1000 {
			fmt.Println(len(inputSeeds), inputSeeds[:10])
			panic("To many seeds!")
		}
	}
	// fmt.Println(inputSeeds)
	// all ranges converted get lowest start
	var result = 10000000000
	for _, seed := range inputSeeds {
		result = min(result, seed.start)
	}

	fmt.Println("Answer: ", result)

	return result
}
