package day1

import (
	"aoc/2023/common"
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()

	var sum int = 0

	for scanner.Scan() {
		// get al integers from string
		var numbers []rune
		for _, c := range scanner.Text() {
			if unicode.IsDigit(c) {
				numbers = append(numbers, c)
			}
		}

		// combine first and last charcter number to int
		num, _ := strconv.Atoi(string(numbers[0]) + string(numbers[len(numbers)-1]))
		sum += num
	}

	fmt.Printf("Sum = %d\n", sum)
	return sum
}

var Word2Num = map[string]int{
	"one":   1,
	"two":   2,
	"three": 3,
	"four":  4,
	"five":  5,
	"six":   6,
	"seven": 7,
	"eight": 8,
	"nine":  9,
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()

	var sum int = 0

	for i := 1; i < 10; i++ {
		Word2Num[strconv.Itoa(i)] = i
	}

	for scanner.Scan() {
		var line = scanner.Text()
		// do index find for every number
		var numFirst string
		var indexFirst int = 10000
		var numLast string
		var indexLast int = -1

		for num := range Word2Num {
			var firstIdx = strings.Index(line, num)
			var lastIdx = strings.LastIndex(line, num)

			if firstIdx >= 0 {
				// found number in line
				if firstIdx < indexFirst {
					indexFirst = firstIdx
					numFirst = num
				}
				if lastIdx > indexLast {
					indexLast = lastIdx
					numLast = num
				}
			}
		}
		// combine first and last combinedNum and add to sum
		combinedNum, _ := strconv.Atoi(fmt.Sprint(Word2Num[numFirst]) + fmt.Sprint(Word2Num[numLast]))
		// fmt.Println(line, Word2Num[numFirst], Word2Num[numLast], combinedNum)
		sum += combinedNum
	}

	fmt.Printf("Sum = %d\n", sum)
	return sum
}
