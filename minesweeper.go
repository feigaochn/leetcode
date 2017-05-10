package main

import "fmt"

func adj(board [][]byte, r, c int) (res int) {
	for i := -1; i < 2; i++ {
		for j := -1; j < 2; j++ {
			if 0 <= r + i && r + i < len(board) && 0 <= c + j && c + j < len(board[r + i]) {
				if board[r + i][c + j] == 'M' {
					res++
				}
			}
		}
	}
	return
}

func updateBoard(board [][]byte, click []int) [][]byte {
	r, c := click[0], click[1]
	if r < 0 || r >= len(board) || c < 0 || c >= len(board[r]) {
		return board
	}
	switch board[r][c] {
	case 'M':
		board[r][c] = 'X'
		return board
	case 'E':
		m := adj(board, r, c)
		if m > 0 {
			board[r][c] = byte(m) + '0'
			return board
		} else {
			board[r][c] = 'B'
			for i := -1; i < 2; i++ {
				for j := -1; j < 2; j++ {
					if !(i == 0 && j == 0) {
						board = updateBoard(board, []int{r + i, c + j})
					}
				}
			}
		}
	}
	return board
}

func printBoard(b [][]byte) {
	for _, row := range b {
		fmt.Println(string(row))
	}
	fmt.Println()
}

func main() {
	board := [][]byte{
		[]byte{'E', 'E', 'E', 'E', 'E'},
		[]byte{'E', 'E', 'M', 'E', 'E'},
		[]byte{'E', 'E', 'E', 'E', 'E'},
		[]byte{'E', 'E', 'E', 'E', 'E'},
	}
	clicks := [][]int{
		[]int{3, 0},
		[]int{1, 2},
	}
	for _, click := range clicks {
		//fmt.Println(board)
		printBoard(board)
		board = updateBoard(board, click)
	}
	printBoard(board)
	//fmt.Println(string(board))

	fmt.Println(string([]byte{'E', 'M', '1', 'B', 'X'}))
}
