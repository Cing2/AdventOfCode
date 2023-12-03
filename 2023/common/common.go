package common

import (
	"bufio"
	"log"
	"os"
)

func FileBuffer(filename string) *bufio.Scanner {

	f, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)

	return scanner
}