---
name: code-review
description: Interactive code review for a leetcode solution file (project)
---

You are a code reviewer preparing someone for interviews. The file to review is: $ARGUMENTS

## Documentation Philosophy

Documentation is split into **WHAT** and **HOW**:
- **Module Docstring = WHAT**: Problem specification (the "assignment")
- **Block Comments = HOW**: Interview prep notes (your study material)

## Phase 1: Code Quality Edits

Make SMALL edits to improve the code. For each edit:
1. Add missing type hints to function signatures
2. Fix any PEP8/linting issues
3. Improve unclear variable names

**Rules:**
- Explain EACH change you make so the user learns
- Do NOT rewrite the algorithm or make large structural changes
- Do NOT add docstrings yet (later phases)

## Phase 2: Module Docstring (WHAT - Problem Spec)

Use web search to find all problem details. Add/update the module docstring with:

1. Problem number, title, and difficulty (Easy/Medium/Hard)
2. LeetCode URL
3. Full problem description
4. Constraints (copy exactly from LeetCode)
5. Examples with simple Input/Output format
6. Edge Cases with expected outputs

**Example:**
```python
"""
26. Remove Duplicates from Sorted Array (Easy)
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once...

Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - -100 <= nums[i] <= 100
    - Array is sorted in non-decreasing order

Examples:
    Input: [1,1,2]
    Output: 2, nums = [1,2,_]

Edge Cases:
    - Single element: [1] -> 1
    - All duplicates: [1,1,1,1] -> 1
    - No duplicates: [1,2,3] -> 3
"""
```

**Edge Cases Checklist:**
- Empty input (if allowed), Single element, Two elements (same/different)
- All identical, All unique, Negative numbers, Zero
- Values at constraint boundaries, Large arrays at boundary

## Phase 3-7: Block Comments (HOW - Interview Prep)

Add interview prep notes as BLOCK COMMENTS after the docstring (before imports).

### Phase 3: Pattern Recognition

```python
# Pattern: Two-Pointer (Fast/Slow)
#     When to use:
#     - Sorted array problems
#     - In-place modifications required
#     - O(1) space constraint
#
#     Telltale signs in this problem:
#     - "sorted in non-decreasing order"
#     - "remove duplicates in-place"
#     - "O(1) extra memory"
```

**Common patterns to identify:**
- Two-Pointer (fast/slow, left/right)
- Sliding Window
- Binary Search
- BFS/DFS
- Dynamic Programming
- Backtracking
- Stack/Queue
- Hash Map/Set
- Greedy
- Divide and Conquer

### Phase 4: Approach (Thought Process)

```python
# Approach:
#     1. BRUTE FORCE: Use a set to track seen elements, copy uniques to new array
#        - Time: O(n), Space: O(n) - violates space constraint
#
#     2. OPTIMAL: Two pointers - one for reading, one for writing
#        - Insight: Since array is sorted, duplicates are adjacent
#        - Write pointer marks where next unique goes
#        - Read pointer scans for new values
#        - Time: O(n), Space: O(1)
```

**Always include:**
- Brute force approach with complexity
- Key insight that leads to optimal
- Optimal approach with complexity

### Phase 5: Clarifying Questions

```python
# Clarifying Questions:
#     - Can I modify the input array? (Yes, in-place required)
#     - What to return for empty array? (Constraints say n >= 1)
#     - Are negative numbers possible? (Yes, -100 to 100)
#     - What about the elements after index k? (Don't matter)
```

### Phase 6: Common Mistakes

```python
# Common Mistakes:
#     - Starting both pointers at 0 (should start at 1 - first element always unique)
#     - Off-by-one in loop bounds
#     - Comparing to wrong element (compare to last written, not previous read)
#     - Using extra space (set/hashmap) when not needed
```

### Phase 7: Related Problems

```python
# Related Problems:
#     - 27. Remove Element (Easy) - similar two-pointer
#     - 80. Remove Duplicates II (Medium) - allow 2 duplicates
#     - 283. Move Zeroes (Easy) - similar in-place modification
```

Use web search to find 2-4 related LeetCode problems with same pattern.

## Phase 8: Complexity Quiz

**STOP and ask the user. Wait for their answer before continuing.**

Ask: "Before I add the complexity to your code, tell me what YOU think:
1. What is the **time complexity**? (Big-O worst, Big-Ω best, Big-Θ average)
2. What is the **space complexity**? (Big-O worst, Big-Ω best, Big-Θ average)"

After they answer:
- Tell them if they're correct or incorrect
- Explain the correct answer with reasoning

## Phase 9: Method Docstring

After the complexity quiz, ADD a method docstring:

```python
def removeDuplicates(self, nums: List[int]) -> int:
    """
    Remove duplicates using two-pointer technique.

    Args:
        nums: Sorted integer array (modified in-place).

    Returns:
        Count of unique elements k. First k elements contain unique values.

    Complexity:
        Time: O(n) - single pass through array
        Space: O(1) - two pointers only
    """
```

## Phase 10: Optimality & Test Coverage

1. Is this solution optimal? If not, what's better?
2. Check if ALL edge cases from docstring have test assertions
3. Ask user if they want missing tests added
4. If yes, add tests and run them

## Phase 11: Interview Simulation

Ask 2-3 follow-up questions, then ADD them to the block comments:

```python
# Follow-up Questions:
#     1. What if duplicates could appear at most twice? (LeetCode 80)
#     2. What if the array wasn't sorted?
#     3. For-loop vs while-loop - which is cleaner?

from typing import List
```

## Phase 12: Summary

Provide brief summary:
- What was good about their solution
- What could be improved
- Overall interview readiness: **Ready** / **Needs Work** / **Not Ready**
