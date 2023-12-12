package day10

import (
	"testing"
	"fmt"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day10.txt")
	var expected = 8
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	var result = Part2("../samples/day10_23.txt")
	var expected = 10
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}
