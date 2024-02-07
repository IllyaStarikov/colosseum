//
//  415-add-strings.swift
//  leetcode
//
//  Created by Illya Starikov on 09/16/19.
//  Copyright 2019. Illya Starikov. All rights reserved.
//

import Foundation

class Solution {
    func getShorterAndLongerString(_ s1: String, _ s2: String) -> (String, String) {
        return s1.count < s2.count ? (s1, s2) : (s2, s1)
    }

    func addStrings(_ num1: String, _ num2: String) -> String {
        let (shorterString, longerString) = getShorterAndLongerString(num1, num2)
        let lengthOfMinimumString = shorterString.count

        let array1 = Array(num1), array2 = Array(num2)

        var added = String()
        var carryover = 0

        for index in 0..<lengthOfMinimumString {
            let element1 = String(array1[array1.count - index - 1])
            let element2 = String(array2[array2.count - index - 1])

            let result = Int(element1)! + Int(element2)! + carryover
            carryover = result < 10 ? 0 : 1

            added.insert(String(result).last!, at: added.startIndex)
        }

        if carryover != 0 {
            added.insert("1", at: added.startIndex)
        }

        var restOfString = ""
        if num1.count != num2.count {
            restOfString = String(Array(longerString)[0...longerString.count - shorterString.count - 1])
        }

        return added + restOfString
    }
}


// TEST CASES
let solution = Solution()

// print(solution.addStrings("1009", "101"))
// print(solution.addStrings("", "101"))
// print(solution.addStrings("101", ""))
// print(solution.addStrings("999", "999"))
// print(solution.addStrings("0", "0"))
print(solution.addStrings("9", "99"))
