package main

import "fmt"

func updateMatrix(matrix [][]int) [][]int {
	nrow, ncol := len(matrix), len(matrix[0])
	queue := make([]int, nrow * ncol * 2)
	head, ins := 0, 0
	for r := range matrix {
		for c := range matrix[r] {
			//fmt.Println(r, c, matrix[r][c])
			if matrix[r][c] == 0 {
				queue[ins] = r * ncol + c
				ins++
			} else {
				matrix[r][c] = nrow * ncol * 10
			}
		}
	}
	for head < ins {
		v := queue[head]
		head++
		r, c := v / ncol, v % ncol
		if r - 1 >= 0 && matrix[r - 1][c] > matrix[r][c] + 1 {
			matrix[r - 1][c] = matrix[r][c] + 1
			queue[ins] = (r - 1) * ncol + c
			ins++
		}
		if r + 1 < nrow && matrix[r + 1][c] > matrix[r][c] + 1 {
			matrix[r + 1][c] = matrix[r][c] + 1
			queue[ins] = (r + 1) * ncol + c
			ins++
		}
		if c - 1 >= 0 && matrix[r][c - 1] > matrix[r][c] + 1 {
			matrix[r][c - 1] = matrix[r][c] + 1
			queue[ins] = (r) * ncol + c - 1
			ins++
		}
		if c + 1 < ncol && matrix[r ][c + 1] > matrix[r][c] + 1 {
			matrix[r][c + 1] = matrix[r][c] + 1
			queue[ins] = (r) * ncol + c + 1
			ins++
		}
		//fmt.Println(r, c)
	}
	return matrix
}

func main() {
	fmt.Println(updateMatrix([][]int{
		[]int{0, 0, 0},
		[]int{0, 1, 0},
		[]int{1, 1, 1},
	}))
}
