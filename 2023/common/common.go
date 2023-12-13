package common

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func FileBuffer(filename string) (*bufio.Scanner, *os.File) {
	f, err := os.Open(filename)
	if err != nil {
		fmt.Println("Could not find file")
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(f)

	return scanner, f
}

func StringToInts(str *string, sep string) []int {
	var new = strings.Trim(*str, " ")
	var splits = strings.Split(new, sep)
	var nums []int
	for _, split := range splits {
		if split == "" {
			continue
		}
		num, err := strconv.Atoi(split)
		if err != nil {
			panic(err)
		}
		nums = append(nums, num)
	}
	return nums
}


type Integers interface {
	int64 | int
}

func AbsInt[V Integers](num V) V {
	if num < 0 {
		return -num
	}
	return num
}
