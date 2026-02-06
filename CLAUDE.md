- Do not make changes to my files unless I specifically ask for it.
- Tests should be inlined into the solution file, not in separate test files.
- Use unittest.TestCase for tests, not simple asserts in main.
- Tests should be inline in the solution file with a TestSolution class.
- Each test method should have a descriptive name (test_example_X, test_edge_X).
- Use setUp() to create the Solution instance.
- Do not remove commented-out code in solution files. These are prior solutions kept to show progression.

## LeetCode Solution Documentation Standards

Documentation is split into two parts: **WHAT** (problem spec) and **HOW** (interview prep).

### Module Docstring = WHAT (Problem Specification)
The docstring describes the problem you're solving. This is the "assignment" in an interview.

Must include:
- Problem number, title, and difficulty (Easy/Medium/Hard)
- LeetCode URL
- Full problem description
- Constraints (copy exactly from LeetCode)
- Examples with simple Input/Output format
- Edge cases with expected outputs

### Block Comments = HOW (Interview Prep Notes)
Comments after the docstring describe how to think through the problem. This is your study material.

Must include:
- **Pattern**: Name the algorithm pattern + when to use it + telltale signs
- **Approach**: Brute force first, then optimal with key insight
- **Clarifying Questions**: What to ask interviewer before coding
- **Common Mistakes**: Pitfalls to avoid for this problem
- **Related Problems**: Similar problems for pattern recognition practice
- **Follow-up Questions**: Interviewer follow-ups to practice

### Method Docstring
Must include:
- Brief description of the approach/technique
- Args with types and descriptions
- Returns with type and description
- Complexity (Time and Space with explanations)

### Example Structure

```python
#!/usr/bin/env python3
"""
26. Remove Duplicates from Sorted Array (Easy)
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order...

Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - -100 <= nums[i] <= 100

Examples:
    Input: [1,1,2]
    Output: 2, nums = [1,2,_]

Edge Cases:
    - Single element: [1] -> 1
    - All duplicates: [1,1,1,1] -> 1
"""

# Pattern: Two-Pointer (Fast/Slow)
#     When to use: sorted arrays, in-place modifications, O(1) space
#     Telltale signs: "sorted", "in-place", "O(1) extra memory"
#
# Approach:
#     1. BRUTE FORCE: Set + new array -> O(n) time, O(n) space
#     2. OPTIMAL: Two pointers -> O(n) time, O(1) space
#        - Insight: sorted means duplicates are adjacent
#
# Clarifying Questions:
#     - Modify in-place? (Yes)
#     - Empty array? (n >= 1 per constraints)
#
# Common Mistakes:
#     - Starting pointers at 0 instead of 1
#     - Comparing to previous read instead of last written
#
# Related Problems:
#     - 27. Remove Element (Easy)
#     - 80. Remove Duplicates II (Medium)
#
# Follow-up Questions:
#     1. What if duplicates allowed twice? (LC 80)
#     2. What if array unsorted?

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates using two-pointer technique.

        Args:
            nums: Sorted integer array (modified in-place).

        Returns:
            Count of unique elements k.

        Complexity:
            Time: O(n) - single pass
            Space: O(1) - two pointers only
        """
        ...
```
