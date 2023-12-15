package day1

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day1_1.txt")
	var expected = 142
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	var result = Part2("../samples/day1_2.txt")
	var expected = 281
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}
