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