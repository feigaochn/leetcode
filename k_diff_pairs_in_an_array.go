package main

import (
	"sort"
	"fmt"
)

func findPairs(nums []int, k int) int {
	r := 0
	sort.Ints(nums)
	//fmt.Println(nums)
	for i, j := 0, 1; j < len(nums); {
		switch {
		case nums[j] - nums[i] < k: j++
		case nums[j] - nums[i] == k:
			r++
			for j < len(nums) && nums[j] - nums[i] == k {
				j++
			}
		case nums[j] - nums[i] > k: i++
			if i == j {
				j++
			}
		}
	}
	return r
}

func main() {
	fmt.Println(findPairs([]int{3, 1, 4, 1, 5}, 2))
	fmt.Println(findPairs([]int{3, 1, 4, 1, 5}, 0))
	fmt.Println(findPairs([]int{3, 1, 4, 2, 5}, 1))
}
