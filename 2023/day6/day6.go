package day6

import (
	"aoc/2023/common"
	"strconv"
	"strings"
)

func chargeBeatsRecord(charge int, time int, record int) bool {
	return charge*(time-charge) > record
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	var times []int
	var records []int
	for scanner.Scan() {
		if strings.Contains(scanner.Text(), "Time") {
			var text = strings.Trim(scanner.Text(), "Time:")
			times = common.StringToInts(&text, " ")
		} else {
			var text = strings.Trim(scanner.Text(), "Distance:")
			records = common.StringToInts(&text, " ")
		}
	}

	var sum = 1
	for i, time := range times {
		var winning_charges = 0
		for j := 0; j < time; j++ {
			if chargeBeatsRecord(j, time, records[i]) {
				winning_charges += 1
			}
		}
		sum *= winning_charges
	}

	return sum
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	var time int
	var record int
	var err error

	for scanner.Scan() {
		if strings.Contains(scanner.Text(), "Time") {
			var text = strings.ReplaceAll(strings.Trim(scanner.Text(), "Time:"), " ", "")
			time, err = strconv.Atoi(text)
			if err != nil {
				panic(err)
			}
		} else {
			var text = strings.ReplaceAll(strings.Trim(scanner.Text(), "Distance:"), " ", "")
			record, err = strconv.Atoi(text)
			if err != nil {
				panic(err)
			}
		}
	}

	var winning_charges = 0
	for j := 0; j < time; j++ {
		if chargeBeatsRecord(j, time, record) {
			winning_charges += 1
		}
	}

	return winning_charges
}
