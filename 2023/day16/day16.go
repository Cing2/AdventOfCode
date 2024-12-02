package day16

import (
	"aoc/2023/common"
	"bufio"
	"fmt"
)

type Grid struct {
	rows [][]rune
}

type Pos struct {
	x int
	y int
}

func (a *Pos) Add(b Pos) Pos {
	return Pos{a.x + b.x, a.y + b.y}
}

type Dir int

const (
	North Dir = iota
	South
	West
	East
)

func (d Dir) Dir() Pos {
	switch d {
	case North:
		return Pos{-1, 0}
	case South:
		return Pos{1, 0}
	case East:
		return Pos{0, -1}
	case West:
		return Pos{0, 1}
	default:
		return Pos{0, 0}
	}
}

func parseGrid(scanner *bufio.Scanner) Grid {
	var grid Grid
	for scanner.Scan() {
		grid.rows = append(grid.rows, []rune(scanner.Text()))
	}
	return grid
}

type Node struct {
	pos Pos
	dir Dir
}

func findEnergyStrength(grid *Grid, startNode Node) int {
	var queue = []Node{startNode}
	var visited = map[Node]bool{}
	var positions = map[Pos]bool{}
	// fmt.Println(North, East, South, West)

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		// check if already been
		_, seen := visited[node]
		if seen {
			continue
		}
		visited[node] = true
		positions[node.pos] = true

		nextPos := node.pos.Add(node.dir.Dir())
		// check if position is in grid

		if nextPos.x < 0 || nextPos.x >= len(grid.rows) || nextPos.y < 0 || nextPos.y >= len((grid.rows)[0]) {
			// dead end
			continue
		}
		var char = grid.rows[nextPos.x][nextPos.y]
		// fmt.Println(node, char)
		switch char {
		case '.':
			// pass through
			queue = append(queue, Node{nextPos, node.dir})
		case '\\':
			var newDir Dir
			if node.dir == West || node.dir == North {
				newDir = (node.dir + 3) % 4
			} else {
				newDir = (node.dir + 1) % 4
			}
			queue = append(queue, Node{nextPos, newDir})
		case '/':
			queue = append(queue, Node{nextPos, (node.dir + 2) % 4})
		case '-':
			if node.dir == East || node.dir == West {
				// pass through
				queue = append(queue, Node{nextPos, node.dir})
			} else {
				// split into two
				queue = append(queue, Node{nextPos, East})
				queue = append(queue, Node{nextPos, West})
			}
		case '|':
			if node.dir == South || node.dir == North {
				// pass through
				queue = append(queue, Node{nextPos, node.dir})
			} else {
				// split into two
				queue = append(queue, Node{nextPos, North})
				queue = append(queue, Node{nextPos, South})
			}
		}
	}

	// count distinc positoins
	return len(positions) - 1
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	grid := parseGrid(scanner)

	return findEnergyStrength(&grid, Node{Pos{0, -1}, West})
}

func printGrid(grid *Grid, visited *map[Pos]bool) {
	for i, row := range grid.rows {
		for j, c := range row {
			_, seen := (*visited)[Pos{i, j}]
			if seen {
				fmt.Print("#")
			} else {
				fmt.Print(string(c))
			}
		}
		fmt.Print("\n")
	}
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	grid := parseGrid(scanner)

	// for every position on road get strength
	var maxStrength = 0
	for i := 0; i < len(grid.rows); i++ {
		strengthW := findEnergyStrength(&grid, Node{Pos{i, -1}, West})
		strengthE := findEnergyStrength(&grid, Node{Pos{i, len(grid.rows[0])}, East})
		maxStrength = max(maxStrength, strengthW, strengthE)
	}

	for i := 0; i < len(grid.rows[0]); i++ {
		strengthW := findEnergyStrength(&grid, Node{Pos{-1, i}, South})
		strengthE := findEnergyStrength(&grid, Node{Pos{len(grid.rows), i}, North})
		maxStrength = max(maxStrength, strengthW, strengthE)
	}

	return maxStrength
}
