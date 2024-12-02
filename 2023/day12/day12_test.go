package day12

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day12.txt")
	var expected = 21
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	var result = Part2("../samples/day12.txt")
	var expected = 525152
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}
