/// 98. Validate Binary Search Tree (Medium)
/// https://leetcode.com/problems/validate-binary-search-tree/
///
/// Given the root of a binary tree, determine if it is a valid binary search tree (BST).
///
/// A valid BST is defined as follows:
/// - The left subtree of a node contains only nodes with keys strictly less than the node's key.
/// - The right subtree of a node contains only nodes with keys strictly greater than the node's key.
/// - Both the left and right subtrees must also be binary search trees.
///
/// Constraints:
///     - The number of nodes in the tree is in the range [1, 10^4]
///     - -2^31 <= Node.val <= 2^31 - 1
///
/// Examples:
///     Input: root = [2,1,3]
///     Output: true
///
///     Input: root = [5,1,4,null,null,3,6]
///     Output: false
///     Explanation: Root is 5, right child is 4, which violates BST property.
///
/// Edge Cases:
///     - Single node: [10] -> true
///     - Empty tree: nil -> true
///     - Duplicate values: [1,1] -> false (must be strictly less/greater)
///     - Deep invalid: value valid for parent but invalid for grandparent
///     - INT_MIN/INT_MAX values: edge cases for range bounds
///     - Left-skewed tree: all left children
///     - Right-skewed tree: all right children

// Pattern: DFS with Range Validation
//     When to use:
//     - Tree property validation
//     - Need to track constraints from ancestors
//     - Recursive tree traversal
//
//     Telltale signs in this problem:
//     - "valid binary search tree"
//     - Property must hold for entire subtree
//     - Constraints propagate from root to leaves
//
// Approach:
//     1. NAIVE: For each node, check all left descendants < node < all right descendants
//        - Time: O(n^2), Space: O(h)
//
//     2. IN-ORDER TRAVERSAL: BST in-order gives sorted sequence
//        - Traverse in-order, check if strictly increasing
//        - Time: O(n), Space: O(h)
//
//     3. RANGE VALIDATION (optimal): Pass valid range to each node
//        - Root: (-inf, +inf)
//        - Left child: (parent_min, parent_val)
//        - Right child: (parent_val, parent_max)
//        - Time: O(n), Space: O(h)
//
//     4. CURRENT: Check if each node can be found via BST search from root
//        - Time: O(n * h), Space: O(n) for visited set
//
// Clarifying Questions:
//     - Are duplicate values allowed? (No, strictly less/greater)
//     - How to handle empty tree? (Valid BST)
//     - Node value range? (-2^31 to 2^31-1)
//     - Can we use extra space? (Usually yes)
//
// Common Mistakes:
//     - Only checking immediate children, not entire subtree
//     - Not handling INT_MIN/INT_MAX edge cases
//     - Using <= instead of < for comparisons
//     - Forgetting that right subtree values must also be > all ancestors on left
//
// Related Problems:
//     - 94. Binary Tree Inorder Traversal (Easy) - in-order traversal
//     - 700. Search in a BST (Easy) - BST search
//     - 230. Kth Smallest Element in a BST (Medium) - BST properties
//     - 99. Recover Binary Search Tree (Medium) - fixing invalid BST
//
// Follow-up Questions:
// 1. How would you solve this iteratively?
// 2. What if we allowed duplicate values on the left?
// 3. How would you fix an invalid BST?

import Foundation

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?

    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
}

class Solution {
    private var explored = Set<Int>()

    /// Validate if a binary tree is a valid BST.
    ///
    /// - Parameter root: Root node of the binary tree.
    /// - Returns: True if tree is a valid BST, false otherwise.
    /// - Complexity: Time O(n * h), Space O(n) for visited set
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

// Inline test framework
struct TestCase {
    let name: String
    let test: () -> Bool
}

class TestRunner {
    private var tests: [TestCase] = []
    private var passed = 0
    private var failed = 0

    func test(_ name: String, _ closure: @escaping () -> Bool) {
        tests.append(TestCase(name: name, test: closure))
    }

    func assertEqual<T: Equatable>(_ actual: T, _ expected: T) -> Bool {
        if actual != expected {
            print("  Expected: \(expected), Got: \(actual)")
            return false
        }
        return true
    }

    func run() {
        print("\n==== Running Tests for Validate BST ====\n")

        for testCase in tests {
            print("> \(testCase.name)", terminator: "")

            if testCase.test() {
                print(" PASS")
                passed += 1
            } else {
                print(" FAIL")
                failed += 1
            }
        }

        print("\n==== Test Results ====")
        print("Passed: \(passed)")
        print("Failed: \(failed)")
        print("Total:  \(passed + failed)")

        if failed > 0 {
            exit(1)
        }
    }
}

// Tests
let runner = TestRunner()
let solution = Solution()

runner.test("Single node BST is valid") {
    let bst = TreeNode(10)
    return runner.assertEqual(solution.isValidBST(bst), true)
}

runner.test("Valid BST with left and right children") {
    let bst = TreeNode(10)
    bst.left = TreeNode(5)
    bst.right = TreeNode(15)
    return runner.assertEqual(solution.isValidBST(bst), true)
}

runner.test("Valid BST with nested children") {
    let bst = TreeNode(10)
    bst.left = TreeNode(5)
    bst.right = TreeNode(15)
    bst.right!.left = TreeNode(11)
    bst.right!.right = TreeNode(20)
    return runner.assertEqual(solution.isValidBST(bst), true)
}

runner.test("Invalid BST with duplicate value") {
    let bst = TreeNode(10)
    bst.left = TreeNode(5)
    bst.right = TreeNode(15)
    bst.right!.left = TreeNode(11)
    bst.right!.right = TreeNode(20)
    bst.left!.right = TreeNode(11)
    return runner.assertEqual(solution.isValidBST(bst), false)
}

runner.test("Empty tree is valid") {
    return runner.assertEqual(solution.isValidBST(nil), true)
}

runner.run()
