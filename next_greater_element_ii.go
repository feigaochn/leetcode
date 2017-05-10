package main

import "fmt"

func nextGreaterElements(nums []int) []int {
	n := len(nums)
	if n == 0 {
		return []int{}
	}
	maxv, maxi := nums[0], 0
	for i, v := range nums {
		if v > maxv {
			maxv, maxi = v, i
		}
	}
	if maxi != n - 1 {
		nums = append(nums, nums[:maxi + 1]...)
	}
	res := make([]int, len(nums))
	pos := make([]int, len(nums))

	pos[len(nums) - 1] = len(nums) - 1
	res[len(nums) - 1] = maxv + 1

	for p := len(nums) - 2; p >= 0; p-- {
		pos[p] = p + 1
		res[p] = nums[pos[p]]
		for nums[p] >= res[p] {
			res[p] = res[pos[p]]
			pos[p] = pos[pos[p]]
		}
	}
	for i := range res {
		if res[i] == maxv + 1 {
			res[i] = -1
		}
	}

	//fmt.Println(nums, pos, res)
	return res[:n]
}

func main() {
	arr := []int{1, 8, -1, -100, -1, 222, 1111111, -111111}
	//arr := []int{1, 2, 1}
	fmt.Println(nextGreaterElements(arr))
}
