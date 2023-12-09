package day8

import (
	"aoc/2023/common"
	"bufio"
	"strings"
)

type node struct {
	left  string
	right string
}

type maps struct {
	instructions string
	nodes        map[string]node
}

func parseMap(scanner *bufio.Scanner) maps {
	var i = 0
	var maps = maps{}
	maps.nodes = make(map[string]node)
	for scanner.Scan() {
		if i == 0 {
			maps.instructions = scanner.Text()
			i += 1
			continue
		} else if scanner.Text() == "" {
			continue
		}
		// nodes
		var splits = strings.Split(scanner.Text(), " = ")
		var nodes = strings.Split(strings.Trim(splits[1], "()"), ", ")
		maps.nodes[splits[0]] = node{nodes[0], nodes[1]}
	}

	return maps
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	maps := parseMap(scanner)

	// follow map with instructions
	var instuctionCounter = 0
	var currentNode = "AAA"
	for {
		if currentNode == "ZZZ" {
			break
		}
		// follow node
		var instruction = maps.instructions[instuctionCounter%len(maps.instructions)]
		if instruction == 'L' {
			currentNode = maps.nodes[currentNode].left
		} else {
			currentNode = maps.nodes[currentNode].right
		}
		instuctionCounter += 1
	}

	return instuctionCounter
}

type cycle struct {
	node  string
	round int
}

func findCycle(startingNode string, maps maps) int {
	var instuctionCounter = 0
	var currentNode = startingNode
	for {
		if strings.HasSuffix(currentNode, "Z") {
			return instuctionCounter
		}
		// follow node
		var instruction = maps.instructions[instuctionCounter%len(maps.instructions)]
		if instruction == 'L' {
			currentNode = maps.nodes[currentNode].left
		} else {
			currentNode = maps.nodes[currentNode].right
		}
		instuctionCounter += 1
	}
}

// greatest common divisor (GCD) via Euclidean algorithm
func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

// find Least Common Multiple (LCM) via GCD
func LCM(integers ...int) int {
	result := integers[0] * integers[1] / GCD(integers[0], integers[1])

	for i := 2; i < len(integers); i++ {
		result = LCM(result, integers[i])
	}

	return result
}
func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	maps := parseMap(scanner)

	var cycles []int
	for node, _ := range maps.nodes {
		if strings.HasSuffix(node, "A") {
			cycles = append(cycles, findCycle(node, maps))
		}
	}
	// get smallest common denominator
	var lcm = LCM(cycles...)

	return lcm
}
