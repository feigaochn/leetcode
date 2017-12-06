package main

import (
	"fmt"
	"sort"
)

func minMoves2(nums []int) int {
	res := 0
	sort.Ints(nums)
	mid := nums[len(nums) / 2]
	for _, v := range nums {
		if v < mid {
			res += mid - v
		} else {
			res += v - mid
		}
	}
	return res
}

func main() {
	fmt.Println(minMoves2([]int{1, 2, 3}))  // 2 (2)
	fmt.Println(minMoves2([]int{1, 2, 6}))  // 5 (2)
	fmt.Println(minMoves2([]int{1, 2, 3, 6}))  // 6 (2,3)
}
