package main

import "fmt"

func findAnagrams(s string, p string) []int {
	result := make([]int, 0)
	if len(s) < len(p) {
		return result
	}

	mp := make(map[byte]int)
	for i := 0; i < len(p); i++ {
		mp[p[i]]--
	}

	//fmt.Println(mp)
	for i := 0; i < len(p); i++ {
		v := s[i]
		mp[v]++
		if mp[v] == 0 {
			delete(mp, v)
		}
		//fmt.Println(mp, v)
	}
	if len(mp) == 0 {
		result = append(result, 0)
	}
	//fmt.Println(mp)
	for i := 1; i < len(s) - len(p) + 1; i++ {
		cOut := s[i - 1]
		cIn := s[i - 1 + len(p)]
		mp[cOut]--
		if mp[cOut] == 0 {
			delete(mp, cOut)
		}
		mp[cIn]++
		if mp[cIn] == 0 {
			delete(mp, cIn)
		}
		//fmt.Println(i, mp)
		if len(mp) == 0 {
			result = append(result, i)
		}
	}
	return result
}

func main() {
	fmt.Println(findAnagrams("cbaebabacd", "abc"))
	fmt.Println(findAnagrams("aa", "bb"))
	fmt.Println(findAnagrams("baa", "aa"))
}
