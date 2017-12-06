package main

import "fmt"

func minDistance(word1 string, word2 string) int {
	len1 := len(word1)
	len2 := len(word2)
	var dp = make([][]int, len1 + 1)
	for i := 0; i <= len1; i++ {
		dp[i] = make([]int, len2 + 1)
	}
	//dp[0][0]
	for i := 1; i <= len1; i++ {
		for j := 1; j <= len2; j++ {
			if word1[i - 1] == word2[j - 1] {
				dp[i][j] = dp[i - 1][j - 1] + 1
			} else {
				dp[i][j] = dp[i - 1][j - 1]
				if dp[i][j] < dp[i - 1][j] {
					dp[i][j] = dp[i - 1][j]
				}
				if dp[i][j] < dp[i][j - 1] {
					dp[i][j] = dp[i][j - 1]
				}
			}
		}
	}
	return len1 + len2 - dp[len1][len2] * 2
}

func main() {
	fmt.Println(minDistance("sea", "seat"))
}
