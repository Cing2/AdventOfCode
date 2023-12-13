package day9

import (
	"aoc/2023/common"
	"fmt"
)

func expandOasis(numbers []int) (int, int) {
	var sumLastNumbs = numbers[len(numbers)-1]
	var sumFirstNumbs = numbers[0]
	var nextLeftMult = -1
	var currentRow = numbers
	var nextRow = make([]int, len(numbers)-1)

	for {
		// fmt.Println(currentRow)
		var allZero = true
		for _, num := range currentRow {
			if num != 0 {
				allZero = false
				break
			}
		}
		if allZero {
			break
		}
		// make next row
		for i := 0; i < len(currentRow)-1; i++ {
			nextRow[i] = currentRow[i+1] - currentRow[i]
		}
		sumLastNumbs += nextRow[len(nextRow)-1]
		sumFirstNumbs += nextLeftMult * nextRow[0]
		nextLeftMult *= -1
		// swap rows
		currentRow = nextRow
		nextRow = make([]int, len(currentRow)-1)
	}

	return sumFirstNumbs, sumLastNumbs
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	var sumLeft = 0
	var sumRight = 0
	for scanner.Scan() {
		var text = scanner.Text()
		var left, right = expandOasis(common.StringToInts(&text, " "))
		sumLeft += left
		sumRight += right
	}
	fmt.Println(sumLeft, sumRight)

	return sumRight
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	var sumLeft = 0
	var sumRight = 0
	for scanner.Scan() {
		var text = scanner.Text()
		var left, right = expandOasis(common.StringToInts(&text, " "))
		// fmt.Println(left, right)
		sumLeft += left
		sumRight += right
	}

	return sumLeft
}
