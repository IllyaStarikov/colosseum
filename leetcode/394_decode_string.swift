/// 394. Decode String (Medium)
/// https://leetcode.com/problems/decode-string/
///
/// Given an encoded string, return its decoded string. The encoding rule is:
/// k[encoded_string], where the encoded_string inside the square brackets is
/// being repeated exactly k times. Note that k is guaranteed to be a positive integer.
///
/// You may assume the input string is always valid; no extra white spaces,
/// square brackets are well-formed, etc. The original data does not contain
/// any digits and digits are only for repeat numbers, k.
///
/// Constraints:
///     - 1 <= s.length <= 30
///     - s consists of lowercase English letters, digits, and square brackets '[]'
///     - s is guaranteed to be a valid input
///     - All integers in s are in the range [1, 300]
///
/// Examples:
///     Input: s = "3[a]2[bc]"
///     Output: "aaabcbc"
///
///     Input: s = "3[a2[c]]"
///     Output: "accaccacc"
///
///     Input: s = "2[abc]3[cd]ef"
///     Output: "abcabccdcdcdef"
///
/// Edge Cases:
///     - Single character repeat: "10[a]" -> "aaaaaaaaaa"
///     - Empty brackets: "3[]" -> ""
///     - No brackets: "abc" -> "abc"
///     - Deeply nested: "2[3[a]b]" -> "aaabaaab"
///     - Multiple consecutive: "3[a]3[b]" -> "aaabbb"

// Pattern: Stack-based Parsing
//     When to use:
//     - Nested structure parsing (brackets, parentheses)
//     - Need to track state at multiple levels
//     - LIFO order of processing
//
//     Telltale signs in this problem:
//     - "k[encoded_string]" nested pattern
//     - Brackets indicate scope/context
//     - Need to build strings at different nesting levels
//
// Approach:
//     1. RECURSIVE: Parse recursively, handling nested brackets
//        - Time: O(maxK * n), Space: O(n) for recursion stack
//
//     2. STACK: Use stack to track numbers and strings at each level
//        - Push current state when seeing '[', pop when seeing ']'
//        - Time: O(maxK * n), Space: O(n)
//
//     3. REGEX (current): Iteratively replace innermost patterns
//        - Find innermost k[...], replace with expansion
//        - Time: O(maxK * n), Space: O(n)
//
// Clarifying Questions:
//     - Can brackets be nested? (Yes)
//     - Is k always present before brackets? (Yes, problem guarantees valid input)
//     - Can k be multi-digit? (Yes, up to 300)
//     - Empty brackets allowed? (Not specified, handle gracefully)
//
// Common Mistakes:
//     - Not handling nested brackets correctly
//     - Integer overflow for large k values
//     - Not handling multi-digit numbers
//     - Off-by-one in string index manipulation
//
// Related Problems:
//     - 726. Number of Atoms (Hard) - similar nested parsing
//     - 1087. Brace Expansion (Medium) - string generation
//     - 772. Basic Calculator III (Hard) - expression parsing
//
// Follow-up Questions:
// 1. How would you handle invalid input?
// 2. What if k could be negative?
// 3. Stack vs recursive - which is more memory efficient?

import Foundation

class Solution {
    /// Decode encoded string using regex-based iterative replacement.
    ///
    /// - Parameter s: Encoded string in format k[encoded_string].
    /// - Returns: Decoded string with patterns expanded.
    /// - Complexity: Time O(maxK * n), Space O(n)
    func decodeString(_ s: String) -> String {
        var stringMutable = s

        let pattern = #"(\d+)\[(\w*?)\]"#
        let regex = try! NSRegularExpression(pattern: pattern, options: [])

        while let match = regex.firstMatch(in: stringMutable, options: [], range: NSRange(stringMutable.startIndex..<stringMutable.endIndex, in: stringMutable)) {
            if let numberRange = Range(match.range(at: 1), in: stringMutable),
              let stringRange = Range(match.range(at: 2), in: stringMutable),
              let wholeRange = Range(match.range(at: 0), in: stringMutable) {

                let string = String(stringMutable[stringRange])
                let repeatCount = Int(stringMutable[numberRange])!
                let replacement = String(repeating: string, count: repeatCount)

                stringMutable = stringMutable.replacingOccurrences(
                    of: stringMutable[wholeRange],
                    with: replacement
                )
            }
        }

        return stringMutable
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
        print("\n==== Running Tests for Decode String ====\n")

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

runner.test("Basic decode with single bracket") {
    return runner.assertEqual(solution.decodeString("3[a]2[bc]"), "aaabcbc")
}

runner.test("Nested brackets") {
    return runner.assertEqual(solution.decodeString("3[a2[c]]"), "accaccacc")
}

runner.test("Mixed with regular characters") {
    return runner.assertEqual(solution.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
}

runner.test("Single character repeat") {
    return runner.assertEqual(solution.decodeString("10[a]"), "aaaaaaaaaa")
}

runner.test("Empty brackets") {
    return runner.assertEqual(solution.decodeString("3[]"), "")
}

runner.test("No brackets") {
    return runner.assertEqual(solution.decodeString("abc"), "abc")
}

runner.run()
