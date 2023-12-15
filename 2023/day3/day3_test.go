package day3

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day3.txt")
	var expected = 4361
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	var result = Part2("../samples/day3.txt")
	var expected = 467835
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}
