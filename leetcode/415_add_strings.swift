/// 415. Add Strings (Easy)
/// https://leetcode.com/problems/add-strings/
///
/// Given two non-negative integers num1 and num2 represented as strings, return
/// the sum of num1 and num2 as a string.
///
/// You must solve the problem without using any built-in library for handling
/// large integers (such as BigInteger). You must also not convert the inputs
/// to integers directly.
///
/// Constraints:
///     - 1 <= num1.length, num2.length <= 10^4
///     - num1 and num2 consist of only digits
///     - num1 and num2 don't have any leading zeros except for zero itself
///
/// Examples:
///     Input: num1 = "11", num2 = "123"
///     Output: "134"
///
///     Input: num1 = "456", num2 = "77"
///     Output: "533"
///
///     Input: num1 = "0", num2 = "0"
///     Output: "0"
///
/// Edge Cases:
///     - Both zeros: "0" + "0" -> "0"
///     - One zero: "0" + "123" -> "123"
///     - Carry propagation: "999" + "1" -> "1000"
///     - Different lengths: "9" + "99" -> "108"
///     - Large numbers: strings with 10000+ digits
///     - Multiple carries: "999" + "999" -> "1998"

// Pattern: Two-Pointer / Elementary Math
//     When to use:
//     - Simulating arithmetic operations
//     - Processing digits from least to most significant
//     - Handling variable-length numeric strings
//
//     Telltale signs in this problem:
//     - "cannot use BigInteger"
//     - "cannot convert to integer"
//     - Need digit-by-digit processing
//
// Approach:
//     1. OPTIMAL: Two-pointer from end with carry
//        - Process from least significant digit (end of string)
//        - Add corresponding digits plus carry
//        - Build result string
//        - Time: O(max(m, n)), Space: O(max(m, n))
//
// Clarifying Questions:
//     - Can inputs have leading zeros? (Only if number is "0")
//     - Can inputs be empty? (No, constraints say length >= 1)
//     - Negative numbers? (No, non-negative only)
//     - How to handle very large numbers? (String manipulation handles it)
//
// Common Mistakes:
//     - Forgetting final carry after loop ends
//     - String index manipulation errors
//     - Not handling different length strings
//     - Building result string inefficiently (prepending vs appending+reverse)
//
// Related Problems:
//     - 2. Add Two Numbers (Medium) - linked list version
//     - 67. Add Binary (Easy) - binary addition
//     - 43. Multiply Strings (Medium) - string multiplication
//     - 66. Plus One (Easy) - increment by 1
//
// Follow-up Questions:
// 1. How would you handle negative numbers?
// 2. Can you optimize string building for very large numbers?
// 3. How would you implement subtraction?

import Foundation

class Solution {
    /// Add two numbers represented as strings without converting to integers.
    ///
    /// - Parameters:
    ///   - num1: First non-negative integer as string.
    ///   - num2: Second non-negative integer as string.
    /// - Returns: Sum of num1 and num2 as a string.
    /// - Complexity: Time O(max(m, n)), Space O(max(m, n))
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
