package day5

import (
	"aoc/2023/common"
	"bufio"
	"strings"
)

type map struct {
	from string
	to string
	ranges []range
}

type range struct {
	
}

func parseInput(scanner *bufio.Scanner) {
	var i = 0
	var seeds []int
	for scanner.Scan() {
		i += 1
		if i == 1 {
			// get seeds
			splits := strings.Split(scanner.Text(), ":")
			seeds = common.StringToInts(&splits[1])
			continue
		}
		var text = scanner.Text()
		if text == ""{
			//skip blank line
			continue
		}
		if strings.Contains(text, "map"){
			// new map start
			var newMap = Map{}
		}
		
	}

}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	parseInput(scanner)


	return 0
}

func Part2(filename string) int {

	return 0
}
