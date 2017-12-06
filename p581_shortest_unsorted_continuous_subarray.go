package main

import "fmt"

func findUnsortedSubarray(nums []int) (ret int) {
	var starts = make([]int, 1)
	starts[0] = 0
	for i := 1; i < len(nums); i++ {
		if nums[i] < nums[i - 1] {
			starts = append(starts, i)
		}
	}
	if len(starts) == 1 {
		return 0
	}
	var a, b = nums[starts[1]], nums[starts[1] - 1]
	for i := 2; i < len(starts); i++ {
		if nums[starts[i]] < a {
			a = nums[starts[i]]
		}
		if nums[starts[i] - 1] > b {
			b = nums[starts[i] - 1]
		}
	}
	var s = 0
	for nums[s] <= a {
		s++
	}
	var e = len(nums) - 1
	for nums[e] >= b {
		e--
	}
	//fmt.Println(s, e)
	return e - s + 1
}

func main() {
	fmt.Println(findUnsortedSubarray([]int{2, 6, 4, 8, 10, 9, 15}))
	fmt.Println(findUnsortedSubarray([]int{2, 6}))
	fmt.Println(findUnsortedSubarray([]int{2}))
	fmt.Println(findUnsortedSubarray([]int{2, 1, 3}))
}
