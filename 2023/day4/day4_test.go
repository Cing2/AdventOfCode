package day4

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	var sum = Part1("../samples/day4.txt")
	var expected = 13
	if sum != expected {
		t.Errorf("Wrong output %d != %d", expected, sum)
	}
}

func TestPart2(t *testing.T) {
	var sum = Part2("../samples/day4.txt")
	fmt.Print(sum)
	var expected = 30
	if sum != expected {
		t.Errorf("Wrong output %d != %d", expected, sum)
	}
}