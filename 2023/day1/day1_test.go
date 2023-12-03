package day1

import (
	"testing"
)

func TestPart1(t *testing.T) {
	var sum = Part1("../samples/day1_1.txt")
	var expected = 142
	if sum != expected {
		t.Errorf("Wrong output %d != %d", expected, sum)
	}
}

func TestPart2(t *testing.T) {
	var sum = Part1("../samples/day1_2.txt")
	var expected = 281
	if sum != expected {
		t.Errorf("Wrong output %d != %d", expected, sum)
	}
}
