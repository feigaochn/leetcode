package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func (t *TreeNode) String() string {
	if t == nil {
		return fmt.Sprint("nil")
	}
	return fmt.Sprintf("(%d (%s) (%s))", t.Val, (t.Left), (t.Right))
}

func convertBST(root *TreeNode) *TreeNode {
	var update func(*TreeNode, int)

	update = func(node *TreeNode, val int) {
		if node == nil {
			return
		}
		node.Val += val
		update(node.Left, val)
		update(node.Right, val)
	}

	if root == nil {
		return nil
	}
	node := TreeNode{root.Val, nil, nil}
	right := convertBST(root.Right)
	if right != nil {
		node.Right = right
		for right.Left != nil {
			right = right.Left
		}
		node.Val += right.Val
	}
	left := convertBST(root.Left)
	if left != nil {
		node.Left = left
		update(node.Left, node.Val)
	}
	return &node
}

func main() {
	t := &TreeNode{1,
		&TreeNode{0,
			&TreeNode{-2, nil, nil},
			nil},
		&TreeNode{4, &TreeNode{3, nil, nil}, nil}}
	fmt.Println(t)
	fmt.Println(convertBST(t))
}
