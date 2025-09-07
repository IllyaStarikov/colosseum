#!/usr/bin/env swift
//
//  394_decode_string_test.swift
//  Tests for LeetCode Problem 394: Decode String
//
//  Author: Illya Starikov
//  License: MIT
//

import Foundation

// Include the solution
class Solution {
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
            print("  ❌ Expected: \(expected), Got: \(actual)")
            return false
        }
        return true
    }
    
    func run() {
        print("\n==== Running Tests for Decode String ====\n")
        
        for testCase in tests {
            print("▶ \(testCase.name)", terminator: "")
            
            if testCase.test() {
                print(" ✅")
                passed += 1
            } else {
                print(" ❌")
                failed += 1
            }
        }
        
        print("\n==== Test Results ====")
        print("✅ Passed: \(passed)")
        print("❌ Failed: \(failed)")
        print("📊 Total:  \(passed + failed)")
        
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