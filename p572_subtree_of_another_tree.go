package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// isSubtree checks if tree t has exactly the same structure and node values with a subtree of s
func isSubtree(s *TreeNode, t *TreeNode) bool {
	if s == nil && t == nil {
		return true
	}
	if (s == nil && t != nil) || (s != nil && t == nil) {
		return false
	}
	here := (s.Val == t.Val) && isSameTree(s.Left, t.Left) && isSameTree(s.Right, t.Right)
	after := isSubtree(s.Left, t) || isSubtree(s.Right, t)
	return here || after
}

func isSameTree(s, t *TreeNode) bool {
	if s == nil && t == nil {
		return true
	}
	if (s == nil && t != nil) || (s != nil && t == nil) {
		return false
	}
	if s.Val == t.Val {
		return isSameTree(s.Left, t.Left) && isSameTree(s.Right, t.Right)
	} else {
		return false
	}
}

func main() {
}
