import "fmt"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func rangeSumBST(root *TreeNode, low int, high int) int {
    var v int = 0
    
    if root == nil{
        return 0
    }
    
    v = rec(root, low, high, v)
    return v
}

func rec(node *TreeNode, L int, R int, v int) int {
    if node.Val < L{
        node.Left = nil
    }
    if node.Val > R{
        node.Right = nil
    }
    if L <= node.Val && node.Val <= R{
        v += node.Val
    }
    if node.Left != nil{
        v = rec(node.Left, L, R, v)
    }
    if node.Right != nil{
        v = rec(node.Right, L, R, v)
    }
    return v
}