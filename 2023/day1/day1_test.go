package day1

import (
	"testing"
)

func TestDay1(t *testing.T) {
	var sum = Day1("../samples/day1_1.txt")
	if sum != 142 {
		t.Errorf("Wrong output %d != %d", 142, sum)
	}
}
