package day

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	var sum = Part1("../samples/day2.txt")
	var expected = 0
	if sum != expected {
		t.Errorf("Wrong output %d != %d", expected, sum)
	}
}

func TestPart2(t *testing.T) {
	var sum = Part2("../samples/day2.txt")
	fmt.Print(sum)
	var expected = 0
	if sum != expected {
		t.Errorf("Wrong output %d != %d", expected, sum)
	}
}