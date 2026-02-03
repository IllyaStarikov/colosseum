#!/usr/bin/env python3
"""
226. Invert Binary Tree (Easy)
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

Inverting a binary tree means swapping every node's left and right children,
recursively through the entire tree.

Constraints:
    - The number of nodes in the tree is in the range [0, 100]
    - -100 <= Node.val <= 100

Examples:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

    Input: root = [2,1,3]
    Output: [2,3,1]

    Input: root = []
    Output: []

Edge Cases:
    - Empty tree: [] -> []
    - Single node: [1] -> [1]
    - Left-skewed: [1,2,None,3] -> [1,None,2,None,3]
    - Right-skewed: [1,None,2,None,3] -> [1,2,None,3,None]
    - Two nodes: [1,2] -> [1,None,2]
    - Symmetric tree: [1,2,2] -> [1,2,2] (unchanged)
"""

# Pattern: DFS / Tree Recursion
#     When to use:
#     - Transform or traverse every node in a tree
#     - Problem has natural recursive substructure (subtrees are same problem)
#     - Need to process children before/after parent (pre/post-order)
#
#     Telltale signs in this problem:
#     - "given the root of a binary tree"
#     - Symmetric operation on left and right subtrees
#     - Output is same structure (tree -> tree)
#
# Approach:
#     1. BRUTE FORCE: BFS with queue, swap children level by level
#        - Time: O(n), Space: O(n) for the queue
#
#     2. OPTIMAL: Recursive DFS, swap children at each node
#        - Insight: inverting a tree = swap left/right, then invert both subtrees
#        - Any traversal order works (pre/post/in-order with care)
#        - Time: O(n), Space: O(h) where h = height (call stack)
#
# Clarifying Questions:
#     - Return a new tree or modify in-place? (Either accepted, in-place is fine)
#     - Empty tree? (Yes, 0 nodes allowed per constraints)
#     - Can values repeat? (Not specified, doesn't matter for structure)
#
# Common Mistakes:
#     - Forgetting base case (null node)
#     - Swapping after recursing (works for pre/post, broken for naive in-order)
#     - In-order trap: swap, recurse left, recurse right — but after swap, the
#       original right is now left, so you'd process it twice and skip the other
#
# Related Problems:
#     - 100. Same Tree (Easy) - recursive comparison of two trees
#     - 101. Symmetric Tree (Easy) - check if tree is its own inverse
#     - 104. Maximum Depth of Binary Tree (Easy) - basic tree DFS
#     - 617. Merge Two Binary Trees (Easy) - recursive dual-tree processing
#
# Follow-up Questions:
#     1. Can you solve this iteratively? (BFS with queue or DFS with stack)
#     2. What if the tree is very deep? (Recursion hits stack limit; use iterative)
#     3. What happens if you invert twice? (Get original back — inversion is self-inverse)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert binary tree using preorder DFS (swap, then recurse).

        Args:
            root: Root of the binary tree (None if empty).

        Returns:
            Root of the inverted tree (same node, modified in-place).

        Complexity:
            Time: O(n) - visits every node exactly once
            Space: O(n) worst (skewed), O(log n) average (balanced) - call stack
        """
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

if __name__ == "__main__":
    s = Solution()

    # Example 1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    result = s.invertTree(root)
    assert result.val == 4
    assert result.left.val == 7
    assert result.right.val == 2
    assert result.left.left.val == 9
    assert result.left.right.val == 6
    assert result.right.left.val == 3
    assert result.right.right.val == 1

    # Example 2: [2,1,3] -> [2,3,1]
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    result = s.invertTree(root)
    assert result.val == 2
    assert result.left.val == 3
    assert result.right.val == 1

    # Edge case: empty tree
    assert s.invertTree(None) is None

    # Edge case: single node
    result = s.invertTree(TreeNode(1))
    assert result.val == 1
    assert result.left is None
    assert result.right is None

    # Edge case: left-skewed tree [1,2,None,3] -> [1,None,2,None,3]
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    result = s.invertTree(root)
    assert result.val == 1
    assert result.left is None
    assert result.right.val == 2
    assert result.right.left is None
    assert result.right.right.val == 3

    # Edge case: right-skewed tree [1,None,2,None,3] -> [1,2,None,3]
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    result = s.invertTree(root)
    assert result.val == 1
    assert result.left.val == 2
    assert result.right is None
    assert result.left.left.val == 3
    assert result.left.right is None

    # Edge case: two nodes [1,2] -> [1,None,2]
    root = TreeNode(1, TreeNode(2))
    result = s.invertTree(root)
    assert result.val == 1
    assert result.left is None
    assert result.right.val == 2

    # Edge case: symmetric tree [1,2,2] -> [1,2,2] (structure unchanged)
    root = TreeNode(1, TreeNode(2), TreeNode(2))
    result = s.invertTree(root)
    assert result.val == 1
    assert result.left.val == 2
    assert result.right.val == 2

    print("All tests passed!")
