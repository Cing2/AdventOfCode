package day3

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	var sum = Part1("../samples/day3.txt")
	var expected = 4361
	if sum != expected {
		t.Errorf("Wrong output %d != %d", expected, sum)
	}
}

func TestPart2(t *testing.T) {
	var sum = Part2("../samples/day3.txt")
	fmt.Print(sum)
	var expected = 467835
	if sum != expected {
		t.Errorf("Wrong output %d != %d", expected, sum)
	}
}
