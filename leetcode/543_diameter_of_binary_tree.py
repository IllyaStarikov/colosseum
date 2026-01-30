#!/usr/bin/env python3
"""
543. Diameter of Binary Tree (Easy)
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.

Constraints:
    - The number of nodes in the tree is in the range [1, 10^4]
    - -100 <= Node.val <= 100

Examples:
    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3]

    Input: root = [1,2]
    Output: 1

Edge Cases:
    - Single node: [1] -> 0 (no edges)
    - Empty tree: None -> 0
    - Linear tree (left-skewed): 1->2->3->4 -> 3 edges
    - Linear tree (right-skewed): 1->2->3->4 -> 3 edges
    - Diameter not through root: longest path in subtree
    - Balanced tree: diameter passes through root
    - Deep subtree: diameter might be entirely in one subtree
"""

# Pattern: DFS with Global State
#     When to use:
#     - Tree traversal problems
#     - Need to track information across subtrees
#     - Computing properties that depend on both children
#     - Path-related tree problems
#
#     Telltale signs in this problem:
#     - "longest path between any two nodes"
#     - "may or may not pass through the root"
#     - Need to consider left + right heights at each node
#
# Approach:
#     1. BRUTE FORCE: For each node, compute height of left and right subtrees
#        - Time: O(n^2), Space: O(h) - recomputes heights multiple times
#
#     2. OPTIMAL: Single DFS pass with global max tracking
#        - Insight: At each node, the diameter through it = left_height + right_height
#        - Track global maximum diameter across all nodes
#        - Return height (1 + max(left, right)) for parent's calculation
#        - Time: O(n), Space: O(h) where h is tree height
#
# Clarifying Questions:
#     - What is the diameter if tree is empty? (0 or handle as edge case)
#     - Is diameter measured in edges or nodes? (Edges)
#     - Can the path go through leaf nodes only? (Yes, any two nodes)
#     - Can node values be negative? (Yes, but values don't affect diameter)
#     - What about single node? (Diameter is 0 - no edges)
#
# Common Mistakes:
#     - Counting nodes instead of edges
#     - Only considering paths through root
#     - Not using global variable for max diameter tracking
#     - Confusing height (nodes) with depth (edges)
#     - Returning diameter instead of height from recursive function
#
# Related Problems:
#     - 104. Maximum Depth of Binary Tree (Easy) - similar recursion pattern
#     - 124. Binary Tree Maximum Path Sum (Hard) - similar global max tracking
#     - 687. Longest Univalue Path (Medium) - path counting in trees
#     - 1522. Diameter of N-Ary Tree (Medium) - generalization
#
# Follow-up Questions:
# 1. What if we needed to return the actual path, not just the length?
# 2. How would you solve this iteratively?
# 3. What if the tree was an n-ary tree instead of binary?

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def build_binary_tree(arr, index=0):
#     if index >= len(arr):
#         return None
#
#     left = 2*index + 1
#     right = 2*index + 2
#
#     return TreeNode(
#         arr[index],
#         build_binary_tree(arr, left),
#         build_binary_tree(arr, right)
#     )

# def length_node(node: Optional[TreeNode], depth=0):
#     if node is None:
#         return depth
#
#     len_left = length_node(node.left, depth+1)
#     len_right = length_node(node.right, depth+1)
#
#     return len_left + len_right
#
#
# def diameter_binary_tree(root: Optional[TreeNode]):
#     if root is None:
#         return 0
#
#     to_explore = [root]
#     max_len = length_node(root)
#
#     while to_explore:
#         node = to_explore.pop()
#         max_len = max(max_len, length_node(node))
#
#         to_explore.extend([node.left, node.right])
#
#     return max_len


def diameter_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Calculate diameter of binary tree using DFS with global max tracking.

    Args:
        root: Root node of the binary tree.

    Returns:
        Length of the longest path (in edges) between any two nodes.

    Complexity:
        Time: O(n) - visit each node once
        Space: O(h) - recursion stack, where h is tree height
    """
    max_diameter = 0

    def height(node: Optional[TreeNode]) -> int:
        nonlocal max_diameter

        if node is None:
            return 0

        left_h = height(node.left)
        right_h = height(node.right)

        diameter_here = left_h + right_h
        max_diameter = max(max_diameter, diameter_here)

        return 1 + max(left_h, right_h)

    height(root)
    return max_diameter


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculate diameter of binary tree.

        Args:
            root: Root node of the binary tree.

        Returns:
            Length of the longest path (in edges) between any two nodes.

        Complexity:
            Time: O(n) - visit each node once
            Space: O(h) - recursion stack, where h is tree height
        """
        return diameter_binary_tree(root)


if __name__ == "__main__":
    # Example 1: [1,2,3,4,5] -> 3
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    # Longest path: 4->2->1->3 or 5->2->1->3 = 3 edges
    root1 = TreeNode(1,
                     TreeNode(2,
                              TreeNode(4),
                              TreeNode(5)),
                     TreeNode(3))
    assert Solution().diameterOfBinaryTree(root1) == 3, "Example 1 failed"

    # Example 2: [1,2] -> 1
    root2 = TreeNode(1, TreeNode(2))
    assert Solution().diameterOfBinaryTree(root2) == 1, "Example 2 failed"

    # Edge case: single node -> 0
    root3 = TreeNode(1)
    assert Solution().diameterOfBinaryTree(root3) == 0, "Single node failed"

    # Edge case: empty tree -> 0
    assert Solution().diameterOfBinaryTree(None) == 0, "Empty tree failed"

    # Diameter doesn't pass through root
    #       1
    #      /
    #     2
    #    / \
    #   3   4
    #  /     \
    # 5       6
    # Longest: 5->3->2->4->6 = 4 edges
    root4 = TreeNode(1,
                     TreeNode(2,
                              TreeNode(3,
                                       TreeNode(5)),
                              TreeNode(4,
                                       None,
                                       TreeNode(6))))
    assert Solution().diameterOfBinaryTree(root4) == 4, "Diameter not through root failed"

    # Straight line (left skewed)
    # 1->2->3->4 = 3 edges
    root5 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert Solution().diameterOfBinaryTree(root5) == 3, "Left skewed failed"

    # Straight line (right skewed)
    # 1->2->3->4 = 3 edges
    root6 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert Solution().diameterOfBinaryTree(root6) == 3, "Right skewed failed"

    # Balanced tree
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    # Diameter: 4->2->1->3->7 = 4 edges
    root7 = TreeNode(1,
                     TreeNode(2, TreeNode(4), TreeNode(5)),
                     TreeNode(3, TreeNode(6), TreeNode(7)))
    assert Solution().diameterOfBinaryTree(root7) == 4, "Balanced tree failed"

    print("All tests passed!")
