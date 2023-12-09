package day8

import (
	"aoc/2023/common"
	"bufio"
	"fmt"
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

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	maps := parseMap(scanner)
	// fmt.Println(maps)
	var currentNodes []string
	for node, _ := range maps.nodes {
		if strings.HasSuffix(node, "A") {
		currentNodes = append(currentNodes, node)
		}
	}
	fmt.Println(currentNodes)

	var instuctionCounter = 0
	for {
		var atEnd = true
		for _, node := range currentNodes {
			if !strings.HasSuffix(node, "Z") {
				atEnd = false
			}
		}
		if atEnd {
			break
		}
		// follow nodes
		var instruction = maps.instructions[instuctionCounter%len(maps.instructions)]
		if instruction == 'L' {

		for i, currentNode := range currentNodes {
			currentNodes[i] = maps.nodes[currentNode].left
		}
		} else {
		for i, currentNode := range currentNodes {
			currentNodes[i] = maps.nodes[currentNode].right
		}
		}
		instuctionCounter += 1
		if instuctionCounter > 1000000{
			fmt.Println(currentNodes)
			panic("taking to long")
			
		}
	}


	return instuctionCounter
}
