package day11

import (
	"testing"
	"fmt"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day11.txt")
	var expected = 374
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	var result = Part2("../samples/day11.txt", 10)
	var expected = 1030
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}
