//
//  961-n-repeated-element-in-size-2n-array.swift
//  leetcode
//
//  Created by Illya Starikov on 09/16/19.
//  Copyright 2019. Illya Starikov. All rights reserved.
//

class Solution {
    func repeatedNTimes(_ A: [Int]) -> Int {
        var values = [Int: Int]()

        for element in A {
            if values[element] == nil {
                values[element] = 0
            }

            values[element]! += 1
        }

        return values.max { $0.value < $1.value }!.key
    }
}

// CLAUDE-CODE BEGIN
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
        print("\n==== Running Tests for N-Repeated Element ====\n")

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

runner.test("Basic case with 3 repeated") {
    return runner.assertEqual(solution.repeatedNTimes([1, 2, 3, 3]), 3)
}

runner.test("Multiple repeats of 2") {
    return runner.assertEqual(solution.repeatedNTimes([2, 1, 2, 5, 3, 2]), 2)
}

runner.test("Alternating pattern with 5") {
    return runner.assertEqual(solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]), 5)
}

runner.test("Repeated at end") {
    return runner.assertEqual(solution.repeatedNTimes([1, 2, 2, 3]), 2)
}

runner.test("Minimum size array") {
    return runner.assertEqual(solution.repeatedNTimes([1, 1, 2, 3]), 1)
}

runner.test("Large repeated number") {
    return runner.assertEqual(solution.repeatedNTimes([9000, 9000, 1, 2]), 9000)
}

runner.run()
// CLAUDE-CODE END
