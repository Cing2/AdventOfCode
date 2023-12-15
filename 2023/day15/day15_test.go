package day15

import (
	"testing"
	"fmt"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day15.txt")
	var expected = 1320
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	var result = Part2("../samples/day15.txt")
	var expected = 145
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}
