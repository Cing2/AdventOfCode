package day1

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"unicode"
)

func Day1(filename string) int {
	f, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)

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
		if err != nil {
			panic(err)
		}
		sum += num
	}

	fmt.Printf("Sum = %d", sum)
	return sum
}
