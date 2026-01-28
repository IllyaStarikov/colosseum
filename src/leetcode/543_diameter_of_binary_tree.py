#!/usr/bin/env python3
"""
Module description

Author: Illya Starikov
Date: 2026-01-27
License: MIT
"""

# Definition for a binary tree node.
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

    print("All tests passed!")
