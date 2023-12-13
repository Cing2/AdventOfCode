package day10

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	var result = Part1("../samples/day10.txt")
	var expected = 8
	fmt.Println("Result: ", result)
	if result != expected {
		t.Errorf("Wrong output %d != %d", expected, result)
	}
}

func TestPart2(t *testing.T) {
	var samples = map[string]int{
		"../samples/day10_1.txt": 1,
		"../samples/day10_2.txt": 4,
		"../samples/day10_23.txt": 10,
	}

	for sample, expected := range samples {
		var result = Part2(sample)
		fmt.Println("Result: ", result)
		if result != expected {
			t.Errorf("Wrong output %d != %d", expected, result)
		}
	}
}
