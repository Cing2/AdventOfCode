package day5

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day5.txt")
	var expected = 35
	fmt.Print(result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	var result = Part2("../samples/day5.txt")
	var expected = 46
	fmt.Print(result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}
