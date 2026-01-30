/// 961. N-Repeated Element in Size 2N Array (Easy)
/// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
///
/// You are given an integer array nums with the following properties:
/// - nums.length == 2 * n
/// - nums contains n + 1 unique elements
/// - Exactly one element of nums is repeated n times
///
/// Return the element that is repeated n times.
///
/// Constraints:
///     - 2 <= n <= 5000
///     - nums.length == 2 * n
///     - 0 <= nums[i] <= 10^4
///     - nums contains n + 1 unique elements, one repeated n times
///
/// Examples:
///     Input: nums = [1,2,3,3]
///     Output: 3
///
///     Input: nums = [2,1,2,5,3,2]
///     Output: 2
///
///     Input: nums = [5,1,5,2,5,3,5,4]
///     Output: 5
///
/// Edge Cases:
///     - Minimum size: [1,1,2,3] -> 1
///     - Repeated at end: [1,2,2,3] -> 2
///     - Alternating pattern: [5,1,5,2,5,3,5,4] -> 5
///     - Large repeated number: [9000,9000,1,2] -> 9000
///     - All at beginning: [1,1,1,2,3,4] -> 1

// Pattern: Hash Map / Frequency Counting
//     When to use:
//     - Finding duplicates or frequencies
//     - Counting occurrences
//     - Element that appears more than others
//
//     Telltale signs in this problem:
//     - "repeated n times"
//     - Fixed structure (n+1 unique, one repeated)
//     - Need to find the element with specific frequency
//
// Approach:
//     1. HASH MAP (current): Count frequency of each element
//        - First element seen twice is the answer
//        - Time: O(n), Space: O(n)
//
//     2. OPTIMAL: Since element repeats n times in 2n array,
//        two occurrences must be within distance 3
//        - Check adjacent and skip-one neighbors
//        - Time: O(n), Space: O(1)
//
//     3. SORTING: Sort and find consecutive duplicates
//        - Time: O(n log n), Space: O(1)
//
// Clarifying Questions:
//     - Is the repeated element guaranteed to exist? (Yes)
//     - Can there be multiple elements repeated? (No, exactly one)
//     - What's the range of values? (0 to 10^4)
//     - Minimum array size? (4 elements, n=2)
//
// Common Mistakes:
//     - Overcomplicating when simple hash set works
//     - Not using the problem's structure (n repeats in 2n)
//     - Returning count instead of element
//
// Related Problems:
//     - 136. Single Number (Easy) - finding unique element
//     - 169. Majority Element (Easy) - element appearing > n/2 times
//     - 229. Majority Element II (Medium) - elements appearing > n/3 times
//     - 287. Find the Duplicate Number (Medium) - cycle detection
//
// Follow-up Questions:
// 1. Can you solve this in O(1) space?
// 2. Why must the repeated element appear within distance 3?
// 3. How would you handle if there could be multiple repeated elements?

class Solution {
    /// Find the element repeated n times in array of size 2n.
    ///
    /// - Parameter A: Array of 2n integers with one element repeated n times.
    /// - Returns: The element that is repeated n times.
    /// - Complexity: Time O(n), Space O(n)
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
