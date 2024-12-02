package day7

import (
	"aoc/2023/common"
	"bufio"
	"sort"
	"strconv"
	"strings"
)

type hand struct {
	cards    string
	bid      int
	strength int
}

func getHandStrength(cards string, includeJoker bool) int {
	// determine type of cards
	// counts how many unique cards
	var uniqueC = map[rune]int{}
	for _, c := range cards {
		i, ok := uniqueC[c]
		if ok {
			uniqueC[c] = i + 1
		} else {
			uniqueC[c] = 1
		}
	}

	jokers, ok := uniqueC['J']
	if includeJoker && ok {
		// add jokers to heighest unique
		delete(uniqueC, 'J')
		var heighestC rune
		var heighestV int
		for c, v := range uniqueC {
			if v > heighestV {
				heighestV = v
				heighestC = c
			}
		}
		uniqueC[heighestC] += jokers
	}

	if len(uniqueC) == 5 {
		// all unique
		return 0
	} else if len(uniqueC) == 4 {
		// one pair
		return 1
	} else if len(uniqueC) == 3 {
		for _, v := range uniqueC {
			if v == 3 {
				// three of a kind
				return 3
			}
		}
		// two pair
		return 2
	} else if len(uniqueC) == 2 {
		for _, v := range uniqueC {
			if v == 4 {
				// four of a kind
				return 5
			}
		}
		// full house
		return 4
	} else {
		// five of a kind
		return 6
	}
}

var cardsOrder = "AKQJT98765432"
var jokerOrder = "AKQT98765432J"

func parseHands(scanner *bufio.Scanner, useJoker bool) []hand {
	var hands []hand
	for scanner.Scan() {
		var splits = strings.Split(scanner.Text(), " ")
		if len(splits[0]) != 5 {
			panic("a hand must have 5 cards")
		}
		bid, err := strconv.Atoi(splits[1])
		if err != nil {
			panic(err)
		}
		hands = append(hands, hand{splits[0], bid, getHandStrength(splits[0], useJoker)})
	}
	return hands
}

func sortHands(hands []hand, useOrder string) {
	sort.Slice(hands, func(i, j int) bool {
		if hands[i].strength == hands[j].strength {
			// if hand have the same type check cards relative order
			for k, c := range hands[i].cards {
				if strings.Index(useOrder, string(c)) != strings.Index(useOrder, string(hands[j].cards[k])) {
					// if not same card, higher index is lower value
					return strings.Index(useOrder, string(c)) > strings.Index(useOrder, string(hands[j].cards[k]))
				}
			}
		}
		return hands[i].strength < hands[j].strength
	})
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	hands := parseHands(scanner, false)

	// sort hands
	sortHands(hands, cardsOrder)

	var sum int
	for i, hand := range hands {
		sum += (i + 1) * hand.bid
	}

	return sum
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	hands := parseHands(scanner, true)

	// sort hands
	sortHands(hands, jokerOrder)

	var sum int
	for i, hand := range hands {
		sum += (i + 1) * hand.bid
	}

	return sum
}
