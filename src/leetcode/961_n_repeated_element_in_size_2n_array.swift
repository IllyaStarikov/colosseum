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

