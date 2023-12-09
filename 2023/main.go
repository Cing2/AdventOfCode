package main

import (
	"aoc/2023/day1"
	"aoc/2023/day2"
	"aoc/2023/day3"
	"aoc/2023/day4"
	"aoc/2023/day5"
	"aoc/2023/day6"
	"aoc/2023/day7"
	"flag"
	"fmt"
	"html/template"
	"os"
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

func main() {
	run_day := flag.Int("d", 1, "Specify day to run")
	make_new := flag.Bool("new", false, "Make file for new day")
	flag.Parse()

	if *make_new {
		fmt.Printf("Creating folder for day %d", *run_day)
		createNewDay(*run_day)
		return
	}

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
	case 4:
		day4.Part1(file_name)
		day4.Part2(file_name)
	case 5:
		day5.Part1(file_name)
		day5.Part2(file_name)
	case 6:
		fmt.Println("Part 1: ", day6.Part1(file_name))
		fmt.Println("Part 2: ", day6.Part2(file_name))
	case 7:
		fmt.Println("Part 1: ", day7.Part1(file_name))
		fmt.Println("Part 2: ", day7.Part2(file_name))
	}
}
