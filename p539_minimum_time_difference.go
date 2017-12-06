package main

import (
	"sort"
	"fmt"
)

func findMinDifference(timePoints []string) int {
	times := make([]int, len(timePoints))
	for ts := range timePoints {
		var h, m int
		fmt.Sscanf(timePoints[ts], "%d:%d", &h, &m)
		times[ts] = h * 60 + m
	}
	sort.Ints(times)
	times = append(times, times[0] + 24 * 60)
	res := 26 * 60
	for i := 0; i < len(timePoints); i++ {
		if times[i + 1] - times[i] < res {
			res = times[i + 1] - times[i]
		}
	}
	return res
}

func main() {
	fmt.Println(findMinDifference([]string{"23:59", "00:00"}))
}
