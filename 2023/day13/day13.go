package day13

import (
	"aoc/2023/common"
	"bufio"
)

type pattern struct {
	rows    []string
	columns []string
}

func parsePatterns(scanner *bufio.Scanner) []pattern {
	var patterns []pattern
	var nextPattern pattern

	for scanner.Scan() {
		if scanner.Text() == "" {
			patterns = append(patterns, nextPattern)
			nextPattern = pattern{}
			continue
		}
		nextPattern.rows = append(nextPattern.rows, scanner.Text())
		for i, c := range scanner.Text() {
			if len(nextPattern.columns) == i {
				nextPattern.columns = append(nextPattern.columns, string(c))
			} else {
				nextPattern.columns[i] += string(c)
			}
		}
	}
	patterns = append(patterns, nextPattern)

	return patterns
}

func findInflection(lines *[]string) int {
	for i := 0; i < len(*lines)-1; i++ {
		// check if line is inflected
		for diff := 0; diff < len(*lines)-1; diff++ {
			if i-diff < 0 || i+1+diff > len(*lines)-1 {
				// all lines match
				return i + 1
			}
			if (*lines)[i-diff] != (*lines)[i+1+diff] {
				// lines are not the same
				break
			}
		}
	}
	return 0
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	patterns := parsePatterns(scanner)

	// find inflection points
	var sum = 0
	for _, pattern := range patterns {
		sum += 100 * findInflection(&pattern.rows)
		sum += findInflection(&pattern.columns)
	}

	return sum
}

func findInflectionSmudge(lines *[]string) int {
	for i := 0; i < len(*lines)-1; i++ {
		// check if line is inflected
		var smudged = false
		for diff := 0; diff < len(*lines)-1; diff++ {
			if i-diff < 0 || i+1+diff > len(*lines)-1 {
				// all lines match
				if smudged {
					return i + 1
				}
				// only return a smudged reflection
				break
			}
			if (*lines)[i-diff] != (*lines)[i+1+diff] {
				// lines are not the same
				if !smudged {
					// check if smudge is possible
					var diffs = 0
					for j, c := range (*lines)[i-diff] {
						if byte(c) != (*lines)[i+1+diff][j] {
							diffs += 1
							if diffs > 1 {
								// more then 1 smudge not possible
								break
							}
						}
					}
					if diffs == 1 {
						// use smudge
						smudged = true
						continue
					}
				}
				break
			}
		}
	}
	return 0
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	patterns := parsePatterns(scanner)

	// find inflection points
	var sum = 0
	for _, pattern := range patterns {
		sum += 100 * findInflectionSmudge(&pattern.rows)
		sum += findInflectionSmudge(&pattern.columns)
	}

	return sum
}
