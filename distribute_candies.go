package main

import (
	"fmt"
)

// https://leetcode.com/problems/distribute-candies/#/description

func distributeCandies(candies []int) int {
	var kindsCount = make(map[int]int)
	for _, v := range candies {
		kindsCount[v]++
	}
	kinds := len(kindsCount)
	if kinds > len(candies)/2 {
		return len(candies) / 2
	} else {
		return kinds
	}
}

func main() {
	fmt.Println(distributeCandies([]int{1, 1, 2, 2, 3, 3}))
	fmt.Println(distributeCandies([]int{1, 1, 2, 3}))
}
