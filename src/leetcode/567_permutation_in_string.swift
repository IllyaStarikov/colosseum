/// 567. Permutation in String
/// https://leetcode.com/problems/permutation-in-string/
///
/// Given two strings s1 and s2, return true if s2 contains a permutation of s1,
/// or false otherwise. In other words, return true if one of s1's permutations
/// is a substring of s2.
///
/// Author: Illya Starikov
/// Date: 09/12/19
/// Copyright 2019. Illya Starikov. All rights reserved.

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
