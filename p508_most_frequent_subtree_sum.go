package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findFrequentTreeSum(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var sumCount = make(map[int]int)
	var treeSum func(*TreeNode) int
	treeSum = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := treeSum(node.Left)
		right := treeSum(node.Right)
		val := node.Val + left + right
		sumCount[val]++
		return val
	}
	treeSum(root)
	bestCount := 0
	result := []int{}
	for s, c := range sumCount {
		if c > bestCount {
			result = []int{s}
			bestCount = c
		} else if c == bestCount {
			result = append(result, s)
		}
	}
	return result
}

func main() {
	t := &TreeNode{5, &TreeNode{2, nil, nil}, &TreeNode{-3, nil, nil}}
	fmt.Println(findFrequentTreeSum(t))
}
