package main

import "fmt"

func findPoisonedDuration(timeSeries []int, duration int) int {
	r := 0
	last := 0
	for _, v := range timeSeries {
		if v + duration > last {
			if v >= last {
				last = v
			}
			r += v + duration - last
			last = v + duration
		}
	}
	return r
}

func main() {
	fmt.Println(findPoisonedDuration([]int{1, 2}, 2))
}
