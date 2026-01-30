/// 567. Permutation in String (Medium)
/// https://leetcode.com/problems/permutation-in-string/
///
/// Given two strings s1 and s2, return true if s2 contains a permutation of s1,
/// or false otherwise. In other words, return true if one of s1's permutations
/// is the substring of s2.
///
/// Constraints:
///     - 1 <= s1.length, s2.length <= 10^4
///     - s1 and s2 consist of lowercase English letters
///
/// Examples:
///     Input: s1 = "ab", s2 = "eidbaooo"
///     Output: true
///     Explanation: s2 contains one permutation of s1 ("ba")
///
///     Input: s1 = "ab", s2 = "eidboaoo"
///     Output: false
///
/// Edge Cases:
///     - Same strings: "abc", "abc" -> true
///     - s1 longer than s2: "hello", "hi" -> false
///     - Empty s1: "", "abc" -> true (empty is permutation of empty)
///     - Single character: "a", "ab" -> true
///     - Repeated characters: "aab", "aabaa" -> true
///     - No match possible: "abc", "def" -> false

// Pattern: Sliding Window with Frequency Count
//     When to use:
//     - Finding substrings with specific properties
//     - Anagram/permutation matching
//     - Fixed-size window problems
//
//     Telltale signs in this problem:
//     - "permutation is a substring"
//     - Two strings comparison
//     - Looking for character frequency match
//
// Approach:
//     1. BRUTE FORCE: Generate all permutations of s1, check if any is in s2
//        - Time: O(n! * m), Space: O(n!) - way too slow
//
//     2. SORTING (current): Sort s1, slide window over s2 and compare sorted
//        - Time: O(n * m * log(n)), Space: O(n)
//
//     3. OPTIMAL: Sliding window with frequency array
//        - Maintain frequency count of current window
//        - Compare with s1 frequency in O(1) or O(26)
//        - Time: O(n + m), Space: O(1) for fixed 26-char array
//
// Clarifying Questions:
//     - Case sensitive? (Yes, lowercase only)
//     - Empty s1 allowed? (Constraints say >= 1, but good to ask)
//     - Unicode characters? (No, lowercase English only)
//     - What if s1 longer than s2? (Return false)
//
// Common Mistakes:
//     - Not handling s1 longer than s2
//     - Using sorting when frequency count is more efficient
//     - Recreating frequency array each iteration instead of sliding
//     - Off-by-one in window bounds
//
// Related Problems:
//     - 438. Find All Anagrams in a String (Medium) - similar pattern
//     - 76. Minimum Window Substring (Hard) - variable window
//     - 242. Valid Anagram (Easy) - simpler version
//     - 49. Group Anagrams (Medium) - grouping by anagram
//
// Follow-up Questions:
// 1. How would you optimize to O(n) using sliding window?
// 2. What if we needed to return all starting indices?
// 3. How would you handle Unicode characters?

extension String {
    func asArray() -> [Character] {
        return Array(self)
    }
}

extension ArraySlice where Element == Character {
    func asString() -> String {
        return String(self)
    }
}

class Solution {
    var cachedSortedString1 = [String.Element]()

    /// Check if s2 contains any permutation of s1.
    ///
    /// - Parameters:
    ///   - s1: Pattern string to find permutation of.
    ///   - s2: String to search in.
    /// - Returns: True if s2 contains a permutation of s1.
    /// - Complexity: Time O(n * m * log(n)), Space O(n)
    func checkInclusion(_ s1: String, _ s2: String) -> Bool {
        if s1.count > s2.count { return false }
        self.cachedSortedString1 = s1.sorted()

        for index in 0 ... s2.count - s1.count {
            let substring = s2.asArray()[index ..< index + s1.count].asString()

            if permutationSearch(inString: substring) {
                return true
            }
        }

        return false
    }

    func permutationSearch(inString s2: String) -> Bool {
        return self.cachedSortedString1 == s2.sorted()
    }
}

import Foundation

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
        print("\n==== Running Tests for Permutation in String ====\n")

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

runner.test("Permutation exists") {
    return runner.assertEqual(solution.checkInclusion("ab", "eidbaooo"), true)
}

runner.test("Permutation does not exist") {
    return runner.assertEqual(solution.checkInclusion("ab", "eidboaoo"), false)
}

runner.test("Same strings") {
    return runner.assertEqual(solution.checkInclusion("abc", "abc"), true)
}

runner.test("s1 longer than s2") {
    return runner.assertEqual(solution.checkInclusion("hello", "hi"), false)
}

runner.test("Empty s1") {
    return runner.assertEqual(solution.checkInclusion("", "abc"), true)
}

runner.test("Single character match") {
    return runner.assertEqual(solution.checkInclusion("a", "ab"), true)
}

runner.test("Repeated characters") {
    return runner.assertEqual(solution.checkInclusion("aab", "aabaa"), true)
}

runner.run()
