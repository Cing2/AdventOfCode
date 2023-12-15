package day14

import (
	"aoc/2023/common"
	"bufio"
	"fmt"
)

type Dir int

const (
	North Dir = iota
	East
	South
	West
)

type Pos struct {
	x int
	y int
}

func (d Dir) Dir() Pos {
	switch d {
	case North:
		return Pos{-1, 0}
	case South:
		return Pos{1, 0}
	case East:
		return Pos{0, 1}
	case West:
		return Pos{0, -1}
	default:
		return Pos{0, 0}
	}
}

type Platform struct {
	rows [][]byte
}

func parsePlatform(scanner *bufio.Scanner) Platform {
	var platform Platform
	for scanner.Scan() {
		newRow := make([]byte, len(scanner.Bytes()))
		copy(newRow, scanner.Bytes())
		platform.rows = append(platform.rows, newRow)
	}

	return platform
}

func tiltPlatform(platform *Platform, dir Dir) {
	if dir == North || dir == South {
		// loop per column
		for c := 0; c < len(platform.rows); c++ {
			// fall all rocks in direction
			for i := 1; i < len(platform.rows); i++ {
				for j := i; j > 0; j-- {
					// if place is a rock and direction is air
					fromRow, toRow := 0, 0
					if dir == North {
						fromRow, toRow = j, j-1
					} else {
						fromRow, toRow = len(platform.rows)-j-1, len(platform.rows)-j
					}
					if platform.rows[fromRow][c] == byte('O') && platform.rows[toRow][c] == byte('.') {
						// rock falls one place, swap bytes
						platform.rows[fromRow][c], platform.rows[toRow][c] = platform.rows[toRow][c], platform.rows[fromRow][c]
					} else {
						// rock cannot fall further
						break
					}
				}
			}
		}
	} else {
		// loop per row
		for r := 0; r < len(platform.rows); r++ {
			// fall all rocks in direction
			for i := 1; i < len(platform.rows); i++ {
				for j := i; j > 0; j-- {
					// if place is a rock and direction is air
					fromC, toC := 0, 0
					if dir == West {
						fromC, toC = j, j-1
					} else {
						fromC, toC = len(platform.rows[0])-j-1, len(platform.rows[0])-j
					}
					if platform.rows[r][fromC] == byte('O') && platform.rows[r][toC] == byte('.') {
						// rock falls one place, swap bytes
						platform.rows[r][fromC], platform.rows[r][toC] = platform.rows[r][toC], platform.rows[r][fromC]
					} else {
						// rock cannot fall further
						break
					}
				}
			}
		}
	}
}

func countLoadNorth(platform *Platform) int {
	var load = 0
	for i, row := range platform.rows {
		for _, c := range row {
			if c == byte('O') {
				// count weight
				load += len(platform.rows) - i
			}
		}
	}

	return load
}

func printPlatform(platform *Platform) {
	for _, row := range platform.rows {
		for _, c := range row {
			fmt.Print(string(c))
		}
		fmt.Print("\n")
	}
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	platform := parsePlatform(scanner)
	// fmt.Println(platform)

	tiltPlatform(&platform, North)
	// fmt.Println("tilted")
	// fmt.Println(len(platform.rows))

	load := countLoadNorth(&platform)
	return load
}

func performCycle(platform *Platform) {
	tiltPlatform(platform, North)
	tiltPlatform(platform, West)
	tiltPlatform(platform, South)
	tiltPlatform(platform, East)
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	platform := parsePlatform(scanner)

	// performCycle(&platform)
	// printPlatform(&platform)
	var findEnd = 1000000000

	var loadCount = map[int][]int{}
	var i = 0
	for i < 10000 {
		performCycle(&platform)
		i += 1
		load := countLoadNorth(&platform)

		_, ok := loadCount[load]
		if ok {
			loadCount[load] = append(loadCount[load], i)

			pattern := loadCount[load]
			if len(pattern) > 5 {
				// check cycle of 2 apart
				var diff = pattern[len(pattern)-1] - pattern[len(pattern)-3]
				if diff != 1 && diff == pattern[len(pattern)-3]-pattern[len(pattern)-5] {
					// check if cycle reaches 1000000000
					if (findEnd-pattern[len(pattern)-1])%diff == 0 {
						// this cycle goes to end
						// fmt.Println(pattern, load, diff)
						return load
					}
				}
			}
		} else {
			loadCount[load] = []int{i}
		}
	}
	fmt.Println(loadCount)

	return 0
}
