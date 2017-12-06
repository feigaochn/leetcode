package main

import "fmt"

func checkInclusion(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}

	chars := make(map[byte]int)

	for i := 0; i < len(s1); i++ {
		chars[s1[i]]--
	}

	var j = 0
	for j < len(s1) {
		chars[s2[j]] ++
		j++
	}

	for {
		empty := true
		for _, v := range chars {
			if v != 0 {
				empty = false
				break
			}
		}
		if empty {
			return empty
		}
		if j >= len(s2) {
			break
		}
		chars[s2[j - len(s1)]]--
		chars[s2[j]] ++
		j++
	}
	return false
}

func main() {
	fmt.Println(checkInclusion("ab", "eidbaooo"))
	fmt.Println(checkInclusion("ab", "eidboaoo"))
	fmt.Println(checkInclusion("adc", "dcda"))
}
