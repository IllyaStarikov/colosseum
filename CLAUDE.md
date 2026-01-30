- Do not make changes to my files unless I specifically ask for it.
- Tests should be inlined into the solution file, not in separate test files.
- Use simple asserts in main, not unittest suites.
- Do not remove commented-out code in solution files. These are prior solutions kept to show progression.

## LeetCode Solution Documentation Standards

Module docstring must include:
- Problem number, title, and difficulty (Easy/Medium/Hard)
- LeetCode URL
- Full problem description
- Constraints (copy exactly from LeetCode)
- Examples with simple Input/Output format
- Edge cases with expected outputs
- **Pattern**: Name the algorithm pattern + when to use it + telltale signs
- **Approach**: Brute force first, then optimal with key insight
- **Clarifying Questions**: What to ask interviewer before coding
- **Common Mistakes**: Pitfalls to avoid for this problem
- **Related Problems**: Similar problems for pattern recognition practice

Method docstring must include:
- Brief description of the approach/technique
- Args with types and descriptions
- Returns with type and description
- Complexity (Time and Space with explanations)

After code review:
- Add follow-up interview questions as comments after the module docstring
- Ensure ALL edge cases have corresponding test assertions