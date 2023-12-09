package day9

import (
	"testing"
	"fmt"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day9.txt")
	var expected = 114
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
} 

func TestPart2(t *testing.T) {
	var result = Part2("../samples/day9.txt")
	var expected = 2
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}
