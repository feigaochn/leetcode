package main

import "fmt"

func countBattleships(board [][]byte) int {
	r := 0
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			if board[i][j] == 'X' {
				switch {
				case i == 0 && j == 0:
					r++
				case i == 0 && j > 0:
					if board[i][j - 1] == '.' {
						r++
					}
				case j == 0 && i > 0: if board[i - 1][j] == '.' {
					r++
				}
				case i > 0 && j > 0:
					if board[i - 1][j] == '.' && board[i][j - 1] == '.' {
						r++
					}
				}
			}
		}
	}
	return r
}

func main() {
	board := [][]byte{
		[]byte("XX"),
	}
	fmt.Println(board)
	fmt.Println(countBattleships(board))
}
