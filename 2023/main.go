package main

import (
	"aoc/2023/day1"
	"aoc/2023/day2"
	"aoc/2023/day3"
	"flag"
	"fmt"
)

func main() {
	run_day := flag.Int("d", 1, "Specify day to run")
	flag.Parse()

	var file_name = fmt.Sprintf("inputs/day%d.txt", *run_day)

	fmt.Printf("Running Day %d with %s\n", *run_day, file_name)
	switch *run_day {
	case 1:
		day1.Part1(file_name)
		day1.Part2(file_name)
	case 2:
		day2.Part1(file_name)
		day2.Part2(file_name)
	case 3:
		day3.Part1(file_name)
		day3.Part2(file_name)
	}
}
