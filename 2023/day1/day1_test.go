package day1

import (
	"fmt"
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
	var sum = Part2("../samples/day1_2.txt")
	fmt.Print(sum)
	var expected = 281
	if sum != expected {
		t.Errorf("Wrong output %d != %d", expected, sum)
	}
}
