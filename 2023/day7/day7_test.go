package day7

import (
	"testing"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day7.txt")
	var expected = 0
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	var result = Part2("../samples/day7.txt")
	var expected = 0
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}
