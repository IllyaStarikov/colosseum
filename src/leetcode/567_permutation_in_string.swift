//
//  567-permutation-in-string .swift
//  leetcode
//
//  Created by Illya Starikov on 09/12/19.
//  Copyright 2019. Illya Starikov. All rights reserved.
//

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

// // TEST CASES
// let solution = Solution()

// // Sample Input
// assert(solution.checkInclusion("ab", "eidbaooo"))
// assert(!solution.checkInclusion("ab", "eidboaoo"))

// // Normal Cases
// assert(solution.checkInclusion("bo", "eidbaooob"))
// assert(solution.checkInclusion("bo", "eidbaoobo"))
// assert(solution.checkInclusion("bo", "boeidbaoo"))
// assert(solution.checkInclusion("bob", "bboeidbaoo"))

// // Edge Cases
// assert(solution.checkInclusion("", "eidbaooob"))
// assert(!solution.checkInclusion("foo", ""))
