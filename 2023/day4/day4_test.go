package day4

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day4.txt")
	var expected = 13
	fmt.Print(result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	var result = Part2("../samples/day4.txt")
	var expected = 30
	fmt.Print(result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}
