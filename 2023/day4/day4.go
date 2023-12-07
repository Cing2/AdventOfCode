package day4

import (
	"aoc/2023/common"
	"bufio"
	"fmt"
	"strings"
)

type Card struct {
	winning []int
	have    []int
}

func extractCards(scanner *bufio.Scanner) []Card {
	var cards []Card
	for scanner.Scan() {
		// split on :
		var splits = strings.Split(scanner.Text(), ":")
		// split on | for winning and having numbers
		splits = strings.Split(splits[1], "|")

		// get numbers
		newCard := Card{
			common.StringToInts(&splits[0]),
			common.StringToInts(&splits[1]),
		}
		cards = append(cards, newCard)
	}
	return cards
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	cards := extractCards(scanner)

	// for every card check how much we won
	var sum = 0
	for _, card := range cards {
		var similar = 0
		for _, win := range card.winning {
			for _, have := range card.have {
				if win == have {
					if similar == 0 {
						similar = 1
					} else {
						similar *= 2
					}
					break
				}
			}
		}
		sum += similar
	}

	fmt.Printf("Sum = %d\n", sum)
	return sum
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	cards := extractCards(scanner)

	// for every card check how much we won
	var cardCopies []int
	for i := 0; i < len(cards); i++ {
		cardCopies = append(cardCopies, 1)
	}

	for i, card := range cards {
		var similar = 0
		for _, win := range card.winning {
			for _, have := range card.have {
				if win == have {
					similar += 1
					break
				}
			}
		}
		for j := 1; j < (similar + 1); j++ {
			// add new copies based on how many copies of current card we have
			cardCopies[i+j] += cardCopies[i]
		}
	}
	var sum = 0
	for _, v := range cardCopies {
		sum += v
	}

	fmt.Printf("Sum = %d\n", sum)
	return sum
}
