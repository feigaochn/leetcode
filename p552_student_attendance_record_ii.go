package main

import "fmt"

func checkRecord(n int) int {
	var mod int64 = 1e9 + 7

	var lastLL = make([]int64, n + 2)
	var lastPL = make([]int64, n + 2)
	var lastLP = make([]int64, n + 2)
	var lastPP = make([]int64, n + 2)
	var total = make([]int64, n + 2)

	lastLL[2] = 1
	lastLP[2] = 1
	lastPP[2] = 1
	lastPL[2] = 1
	total[0] = 1
	total[1] = 2
	total[2] = 4

	for i := 3; i < n + 1; i++ {
		lastLL[i] = (lastPL[i - 1])
		lastPL[i] = (lastLP[i - 1] + lastPP[i - 1]) % mod

		lastLP[i] = (lastLL[i - 1] + lastPL[i - 1]) % mod
		lastPP[i] = (lastLP[i - 1] + lastPP[i - 1]) % mod

		total[i] = (lastPP[i] + lastPL[i] + lastLP[i] + lastLL[i]) % mod
	}

	//fmt.Println(total)

	var ret int64 = total[n]

	// f + 'A' + (n-1-f)
	for f := 0; f < n; f++ {
		ret = (ret + total[f] * total[n - 1 - f]) % mod
	}
	return int(ret % mod)
}

func main() {
	fmt.Println(checkRecord(100000))
	fmt.Println(checkRecord(1))
}
