package common

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func FileBuffer(filename string) (*bufio.Scanner, *os.File ) {
	f, err := os.Open(filename)
	if err != nil {
		fmt.Println("Could not find file")
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(f)

	return scanner, f
}
