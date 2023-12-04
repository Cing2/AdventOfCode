package main

import (
	"aoc/2023/day1"
	"flag"
	"fmt"
)

func main() {
	run_day := flag.Int("d", 1, "Specify day to run")

	var file_name = fmt.Sprintf("inputs/day%d.txt", *run_day)

	fmt.Printf("Running with %s\n", file_name)
	fmt.Printf("Running Day %d\n", *run_day)
	switch *run_day {
	case 1:
		day1.Part1(file_name)
		day1.Part2(file_name)
	}

}
