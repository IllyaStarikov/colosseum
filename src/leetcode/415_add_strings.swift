//
//  415_add_strings.swift
//  leetcode
//
//  Created by Illya Starikov on 09/16/19.
//  Copyright 2019. Illya Starikov. All rights reserved.
//

import Foundation

class Solution {
    func addStrings(_ num1: String, _ num2: String) -> String {
        let array1 = Array(num1.reversed())
        let array2 = Array(num2.reversed())
        
        var result = ""
        var carry = 0
        var i = 0
        
        while i < array1.count || i < array2.count || carry > 0 {
            let digit1 = i < array1.count ? Int(String(array1[i]))! : 0
            let digit2 = i < array2.count ? Int(String(array2[i]))! : 0
            
            let sum = digit1 + digit2 + carry
            carry = sum / 10
            result = String(sum % 10) + result
            
            i += 1
        }
        
        return result.isEmpty ? "0" : result
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
        print("\n==== Running Tests for Add Strings ====\n")

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

runner.test("Add two regular numbers") {
    return runner.assertEqual(solution.addStrings("123", "456"), "579")
}

runner.test("Add with carry") {
    return runner.assertEqual(solution.addStrings("999", "1"), "1000")
}

runner.test("Add with multiple carries") {
    return runner.assertEqual(solution.addStrings("999", "999"), "1998")
}

runner.test("Add zero to number") {
    return runner.assertEqual(solution.addStrings("0", "123"), "123")
}

runner.test("Add two zeros") {
    return runner.assertEqual(solution.addStrings("0", "0"), "0")
}

runner.test("Add numbers of different lengths") {
    return runner.assertEqual(solution.addStrings("9", "99"), "108")
}

runner.test("Add large numbers") {
    return runner.assertEqual(solution.addStrings("1009", "101"), "1110")
}

runner.run()