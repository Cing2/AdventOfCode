package day11

import (
	"aoc/2023/common"
	"bufio"
)

type Pos struct {
	x int
	y int
}

func (a *Pos) Minus(b *Pos) Pos {
	return Pos{common.AbsInt(a.x - b.x), common.AbsInt(a.y - b.y)}
}

func readGalaxiesExpand(scanner *bufio.Scanner, expandMultiple int) []Pos {
	var universe []string
	var galaxies []Pos
	var i int = 0
	for scanner.Scan() {
		universe = append(universe, scanner.Text())
		// check if row is fully empty then add one to i
		var rowEmpty = true
		for j, c := range scanner.Text() {
			if c == '#' {
				rowEmpty = false
				galaxies = append(galaxies, Pos{i, int(j)})
			}
		}
		if rowEmpty {
			i += expandMultiple
		} else {
			i += 1
		}
	}

	// expand universe column wise
	var length = int(len(universe[0]))
	var expansions int = 0
	for c := int(0); c < length; c++ {
		// if line is empty ie. all .
		var columnEmpty = true
		for r := 0; r < len(universe); r++ {
			if universe[r][c] == '#' {
				columnEmpty = false
				break
			}
		}
		if columnEmpty {
			// for every universe with column greater then c add 1
			for i, gal := range galaxies {
				if gal.y > c+expansions {
					galaxies[i].y += expandMultiple - 1
				}
			}
			expansions += expandMultiple - 1
		}
	}

	return galaxies
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()

	var galaxies = readGalaxiesExpand(scanner, 2)
	// for every pair add dist
	var sum int = 0
	for i := 0; i < len(galaxies)-1; i++ {
		for j := i + 1; j < len(galaxies); j++ {
			dist := galaxies[i].Minus(&galaxies[j])
			sum += dist.x + dist.y
			// sum += 1
		}
	}

	return sum
}

func Part2(filename string, multiple int) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()

	var galaxies = readGalaxiesExpand(scanner, multiple)
	// for every pair add dist
	var sum int = 0
	for i := 0; i < len(galaxies)-1; i++ {
		for j := i + 1; j < len(galaxies); j++ {
			dist := galaxies[i].Minus(&galaxies[j])
			sum += dist.x + dist.y
			// sum += 1
		}
	}

	return sum
}
