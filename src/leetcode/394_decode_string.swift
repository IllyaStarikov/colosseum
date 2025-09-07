//
//  394-decode-string.swift
//  leetcode
//
//  Created by Illya Starikov on 09/15/19.
//  Copyright 2019. Illya Starikov. All rights reserved.
//

import Foundation

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


// TEST CASES
// let solution = Solution()
// assert(solution.decodeString("3[a]2[bc]") == "aaabcbc")
// assert(solution.decodeString("3[a2[c]]") == "accaccacc")
// assert(solution.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
