// public class TreeNode {
//     public var val: Int
//     public var left: TreeNode?
//     public var right: TreeNode?

//     public init(_ val: Int) {
//         self.val = val
//         self.left = nil
//         self.right = nil
//     }
// }

class Solution {
    private var explored = Set<Int>()

    func isValidBST(_ root: TreeNode?) -> Bool {
        explored.removeAll(keepingCapacity: true)
        return traverse(bst: root, fromRoot: root)
    }

    private func traverse(bst: TreeNode?, fromRoot root: TreeNode?) -> Bool {
        if let node = bst {
            if explored.contains(node.val) {
                return false
            }

            let result = validate(node: node, inBST: root)
            explored.insert(node.val)

            return result && traverse(bst: node.left, fromRoot: root) && traverse(bst: node.right, fromRoot: root)
        } else {
            return true
        }
    }

    private func validate(node: TreeNode, inBST bst: TreeNode?) -> Bool {
        if let bst = bst {
            if node.val == bst.val {
                return true
            } else if node.val > bst.val {
                return validate(node: node, inBST: bst.right)
            } else { // node.val < bst.val
                return validate(node: node, inBST: bst.left)
            }
        } else {
            return false
        }
    }
}

// TEST CASES
//    10
//   / \
//  5   15
//     / \
//    11  20
//

// let solution = Solution()

// var bst = TreeNode(10)
// assert(solution.isValidBST(bst))

// bst.left = TreeNode(5)
// bst.right = TreeNode(15)
// assert(solution.isValidBST(bst))

// bst.right!.left = TreeNode(11)
// bst.right!.right = TreeNode(20)
// assert(solution.isValidBST(bst))

// bst.left!.right = TreeNode(11)
// assert(!solution.isValidBST(bst))
