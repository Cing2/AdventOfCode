package day15

import (
	"aoc/2023/common"
	"strconv"
	"strings"
)

func computeHash(seq string) int {
	var current = 0
	for _, c := range seq {
		current += int(c)
		current *= 17
		current = current % 256
	}
	return current
}

func Part1(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	scanner.Scan()
	sequences := strings.Split(scanner.Text(), ",")
	// fmt.Println(sequences)
	var sum = 0
	for _, seq := range sequences {
		res := computeHash(seq)
		// fmt.Println(seq, res)
		sum += res
	}

	return sum
}

type lens struct {
	label         string
	focalStrength int
}

func Part2(filename string) int {
	scanner, f := common.FileBuffer(filename)
	defer f.Close()
	scanner.Scan()
	sequences := strings.Split(scanner.Text(), ",")

	var hashMap = [256][]lens{}
	for _, seq := range sequences {
		if strings.Contains(seq, "-") {
			// label is end removed
			label := seq[:len(seq)-1]
			hash := computeHash(label)

			// remove lens from hash
			for i, lens := range hashMap[hash] {
				if lens.label == label {
					hashMap[hash] = append(hashMap[hash][:i], hashMap[hash][i+1:]...)

				}
			}
		} else {
			// contains =
			label := seq[:len(seq)-2]
			hash := computeHash(label)
			focalStrength, err := strconv.Atoi(string(seq[len(seq)-1]))
			if err != nil {
				panic(err)
			}
			// check if lens is already present
			var alreadyPresent = false
			for i, lens := range hashMap[hash] {
				if lens.label == label {
					hashMap[hash][i].focalStrength = focalStrength
					alreadyPresent = true
					break
				}
			}
			if !alreadyPresent {
				hashMap[hash] = append(hashMap[hash], lens{label, focalStrength})
			}
		}
	}
	// fmt.Println(hashMap)

	// count total focal strenght
	var totalFocalstrength = 0
	for i, lenses := range hashMap {
		for j, lens := range lenses {
			totalFocalstrength += (i + 1) * (j + 1) * lens.focalStrength
		}
	}

	return totalFocalstrength
}
