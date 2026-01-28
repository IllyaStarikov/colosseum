import Foundation

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?

    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
}

class Solution {
    private var explored = Set<Int>()

    func isValidBST(_ root: TreeNode?) -> Bool {
        explored.removeAll(keepingCapacity: true)
        return traverse(bst: root, fromRoot: root)
    }

    private func traverse(bst: TreeNode?, fromRoot root: TreeNode?) -> Bool {
        if let node = bst {
            if explored.contains(node.val) {
                return false
            }

            let result = validate(node: node, inBST: root)
            explored.insert(node.val)

            return result && traverse(bst: node.left, fromRoot: root) && traverse(bst: node.right, fromRoot: root)
        } else {
            return true
        }
    }

    private func validate(node: TreeNode, inBST bst: TreeNode?) -> Bool {
        if let bst = bst {
            if node.val == bst.val {
                return true
            } else if node.val > bst.val {
                return validate(node: node, inBST: bst.right)
            } else { // node.val < bst.val
                return validate(node: node, inBST: bst.left)
            }
        } else {
            return false
        }
    }
}

// CLAUDE-CODE BEGIN
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
        print("\n==== Running Tests for Validate BST ====\n")

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

runner.test("Single node BST is valid") {
    let bst = TreeNode(10)
    return runner.assertEqual(solution.isValidBST(bst), true)
}

runner.test("Valid BST with left and right children") {
    let bst = TreeNode(10)
    bst.left = TreeNode(5)
    bst.right = TreeNode(15)
    return runner.assertEqual(solution.isValidBST(bst), true)
}

runner.test("Valid BST with nested children") {
    let bst = TreeNode(10)
    bst.left = TreeNode(5)
    bst.right = TreeNode(15)
    bst.right!.left = TreeNode(11)
    bst.right!.right = TreeNode(20)
    return runner.assertEqual(solution.isValidBST(bst), true)
}

runner.test("Invalid BST with duplicate value") {
    let bst = TreeNode(10)
    bst.left = TreeNode(5)
    bst.right = TreeNode(15)
    bst.right!.left = TreeNode(11)
    bst.right!.right = TreeNode(20)
    bst.left!.right = TreeNode(11)
    return runner.assertEqual(solution.isValidBST(bst), false)
}

runner.test("Empty tree is valid") {
    return runner.assertEqual(solution.isValidBST(nil), true)
}

runner.run()
// CLAUDE-CODE END
