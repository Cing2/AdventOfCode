package main

import (
	"aoc/2023/day1"
	"aoc/2023/day10"
	"aoc/2023/day11"
	"aoc/2023/day12"
	"aoc/2023/day13"
	"aoc/2023/day14"
	"aoc/2023/day15"
	"aoc/2023/day2"
	"aoc/2023/day3"
	"aoc/2023/day4"
	"aoc/2023/day5"
	"aoc/2023/day6"
	"aoc/2023/day7"
	"aoc/2023/day8"
	"aoc/2023/day9"
	"flag"
	"fmt"
	"html/template"
	"os"
	"time"
)

func writeTemplate(pathTemplate string, output string, day int) {
	t, err := template.ParseFiles(pathTemplate)
	if err != nil {
		panic(err)
	}

	f, err := os.Create(output)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	err = t.Execute(f, day)
	if err != nil {
		panic(err)
	}
}

func createNewDay(day int) {
	// create dir
	if err := os.Mkdir(fmt.Sprintf("day%d", day), os.ModePerm); err != nil {
		panic(err)
	}

	// create go files
	writeTemplate("dayTemplate/day_test.tmpl", fmt.Sprintf("day%d/day%d_test.go", day, day), day)
	writeTemplate("dayTemplate/day.tmpl", fmt.Sprintf("day%d/day%d.go", day, day), day)

	// create input and sample file
	f, err := os.Create(fmt.Sprintf("inputs/day%d.txt", day))
	if err != nil {
		panic(err)
	}
	defer f.Close()
	f2, err := os.Create(fmt.Sprintf("samples/day%d.txt", day))
	if err != nil {
		panic(err)
	}
	defer f2.Close()
}

func RunDay(run_day int) {
	start := time.Now()

	fmt.Println("Running day ", run_day)

	var file_name = fmt.Sprintf("inputs/day%d.txt", run_day)

	var res_part1 int
	var res_part2 int
	var time_part1 time.Time

	switch run_day {
	case 1:
		res_part1 = day1.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day1.Part2(file_name)
	case 2:
		res_part1 = day2.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day2.Part2(file_name)
	case 3:
		res_part1 = day3.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day3.Part2(file_name)
	case 4:
		res_part1 = day4.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day4.Part2(file_name)
	case 5:
		res_part1 = day5.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day5.Part2(file_name)
	case 6:
		res_part1 = day6.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day6.Part2(file_name)
	case 7:
		res_part1 = day7.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day7.Part2(file_name)
	case 8:
		res_part1 = day8.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day8.Part2(file_name)
	case 9:
		res_part1 = day9.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day9.Part2(file_name)
	case 10:
		res_part1 = day10.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day10.Part2(file_name)
	case 11:
		res_part1 = day11.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day11.Part2(file_name, 1000000)
	case 12:
		res_part1 = day12.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day12.Part2(file_name)
	case 13:
		res_part1 = day13.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day13.Part2(file_name)
	case 14:
		res_part1 = day14.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day14.Part2(file_name)
	case 15:
		res_part1 = day15.Part1(file_name)
		time_part1 = time.Now()
		res_part2 = day15.Part2(file_name)
	default:
		return

	}
	elapsed_part1 := time_part1.Sub(start)
	elapsed_part2 := time.Since(time_part1)
	fmt.Printf("Part 1: %d \t took %s\n", res_part1, elapsed_part1)
	fmt.Printf("Part 2: %d \t took %s\n", res_part2, elapsed_part2)
	fmt.Printf("Total time: %s\n", elapsed_part1+elapsed_part2)

}

func main() {
	day := flag.Int("d", 1, "Specify day to run")
	make_new := flag.Bool("new", false, "Make file for new day")
	all := flag.Bool("all", false, "Run all days")
	flag.Parse()

	if *make_new {
		fmt.Printf("Creating folder for day %d", *day)
		createNewDay(*day)
		return
	}
	if *all {
		for i := 1; i <= 14; i++ {
			RunDay(i)
		}
	} else {
		RunDay(*day)
	}
}
