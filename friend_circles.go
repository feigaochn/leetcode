package main

import "fmt"

func findCircleNum(M [][]int) int {
	mark := make([]int, len(M))
	//fmt.Println(mark)
	r := 0
	for i := 0; i < len(M); i++ {
		if mark[i] == 0 {
			r++
			mark[i] = r

			queue := []int{i}
			for len(queue) > 0 {
				top := queue[0]
				queue = queue[1:]
				for j := 0; j < len(M); j++ {
					if M[top][j] == 1 && mark[j] == 0 {
						mark[j] = mark[top]
						queue = append(queue, j)
					}
				}
			}
		}
	}

	return r
}

func main() {
	mat := [][]int{
		[]int{1, 0, 0, 1},
		[]int{0, 1, 1, 0},
		[]int{0, 1, 1, 1},
		[]int{1, 0, 1, 1},
	}
	fmt.Println(findCircleNum(mat))
}
