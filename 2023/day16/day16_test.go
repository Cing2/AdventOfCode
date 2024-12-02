package day16

import (
	"testing"
	"fmt"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day16.txt")
	var expected = 46
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	var result = Part2("../samples/day16.txt")
	var expected = 51
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}
