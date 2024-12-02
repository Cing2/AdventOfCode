package day10

import (
	"aoc/2023/common"
	"fmt"
)

type Dir int

const (
	North Dir = iota
	East
	South
	West
	Start
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
	case Start:
		return Pos{0, 0}
	}
	return Pos{0, 0}
}

type node struct {
	pos  Pos
	from Dir
	dist int
}

func (a *Pos) Add(b Pos) Pos {
	return Pos{a.x + b.x, a.y + b.y}
}

var nodeType = map[rune][]Dir{
	'|': {North, South},
	'-': {East, West},
	'L': {North, East},
	'J': {North, West},
	'7': {South, West},
	'F': {South, East},
	'S': {North, East, West, South},
}

func (a Dir) reverse(b Dir) bool {
	switch a {
	case North:
		return b == South
	case South:
		return b == North
	case East:
		return b == West
	case West:
		return b == East
	}
	return false
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()

	var matrix []string
	var startPos Pos
	var i = 0
	for scanner.Scan() {
		matrix = append(matrix, scanner.Text())
		for j, c := range scanner.Text() {
			if c == 'S' {
				startPos = Pos{i, j}
			}
		}
		i += 1
	}

	// BFS from start
	var visited = map[Pos]int{}
	var queue = []node{{startPos, Start, 0}}
	for len(queue) > 0 {
		var nextNode = queue[0]
		queue = queue[1:]
		// process node other positions
		// check pos in range
		if nextNode.pos.x < 0 || nextNode.pos.x >= len(matrix) ||
			nextNode.pos.y < 0 || nextNode.pos.y >= len(matrix[0]) {
			continue
		}
		var char = matrix[nextNode.pos.x][nextNode.pos.y]
		if char == '.' { //skip . which means empty
			continue
		}
		// check if already visited
		_, ok := visited[nextNode.pos]
		if ok {
			continue
		}

		// process node
		var connectPrevious = false
		var newNode node
		for _, dir := range nodeType[rune(char)] {
			if nextNode.from.reverse(dir) {
				connectPrevious = true
				continue
			}
			// create new node
			newpos := nextNode.pos.Add(dir.Dir())
			newNode = node{newpos, dir, nextNode.dist + 1}

			if nextNode.from == Start {
				// start should add every node
				queue = append(queue, newNode)
			}
		}
		if connectPrevious {
			// only visit node when previous connects
			visited[nextNode.pos] = nextNode.dist
			queue = append(queue, newNode)
		}
	}
	// get max
	var max_dist = 0
	for _, dist := range visited {
		max_dist = max(max_dist, dist)
	}

	return max_dist
}

func printVisited(visited *map[Pos]int, matrix *[]string) {
	for i := 0; i < len(*matrix); i++ {
		for j := 0; j < len((*matrix)[0]); j++ {
			dist, ok := (*visited)[Pos{i, j}]
			if ok {
				fmt.Print(dist)
			} else {
				fmt.Print(".")
			}
		}
		fmt.Print("\n")
	}
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	var matrix []string
	var startPos Pos
	var i = 0
	for scanner.Scan() {
		matrix = append(matrix, scanner.Text())
		for j, c := range scanner.Text() {
			if c == 'S' {
				startPos = Pos{i, j}
			}
		}
		i += 1
	}
	loop := newfindLoop(&matrix, startPos)
	// calculate area under polygon
	area := areaPolygon(&loop)
	// subtract length of loop to find enclosed spaces
	return area - (len(loop)+1)/2 + 1
}

func areaPolygon(vertices *[]Pos) int {
	var sum = 0
	for i := 0; i < len(*vertices)-1; i++ {
		sum += (*vertices)[i].x*(*vertices)[i+1].y - (*vertices)[i+1].x*(*vertices)[i].y
	}
	sum += (*vertices)[len(*vertices)-1].x*(*vertices)[0].y - (*vertices)[0].x*(*vertices)[len(*vertices)-1].y

	return common.AbsInt(sum) / 2
}

func newfindLoop(matrix *[]string, startPos Pos) []Pos {
	var orderVisited []Pos
	for _, dir := range nodeType['S'] {
		orderVisited = []Pos{startPos}
		var foundStart = false
		for {
			nextPos := orderVisited[len(orderVisited)-1].Add(dir.Dir())
			// check pos in range
			if nextPos.x < 0 || nextPos.x >= len(*matrix) || nextPos.y < 0 || nextPos.y >= len((*matrix)[0]) {
				// dead end
				break
			}
			if nextPos == startPos {
				foundStart = true
				break
			}
			var char = (*matrix)[nextPos.x][nextPos.y]
			if char == '.' {
				// dead end
				break
			}

			// check if node connects and what is nextNode
			var nodeConnects = true
			var nextDir Dir
			for _, newDir := range nodeType[rune(char)] {
				if newDir.reverse(dir) {
					nodeConnects = true
					continue
				}
				nextDir = newDir
			}
			if nodeConnects {
				orderVisited = append(orderVisited, nextPos)
				dir = nextDir
			} else {
				// dead end at start
				break
			}
		}
		if foundStart {
			break
		}
	}

	return orderVisited
}
