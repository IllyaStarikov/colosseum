#!/usr/bin/swift

import Foundation

func isUnique(_ word: String) -> Bool {
    var values = [Character: Bool]()

    for character in word {
        if values[character] != nil {
            return false
        }

        values[character] = true
    }

    return true
}

func uint64(from scalar: UnicodeScalar) -> UInt64 {
    return UInt64(scalar.value)
}

func settingBitAt(index: UInt64) -> UInt64 {
    let result = pow(2.0, Double(index))
    return UInt64(Int(result))
}

func isUniqueFast(_ word: String) -> Bool {
    let unicodeCharacterStart = uint64(from: "A".unicodeScalars.first!)
    var byteArray: UInt64 = uint64(from: word.unicodeScalars.first!) - unicodeCharacterStart

    var word = word

    word.remove(at: word.startIndex)

    for character in word {
        let scalar = uint64(from: character.unicodeScalars.first!) - unicodeCharacterStart
        let scalarAsBit = settingBitAt(index: scalar)

        if byteArray & scalarAsBit != 0 {
            return false
        }

        byteArray |= scalarAsBit
    }

    return true
}

print(isUniqueFast("abcxyz"))
print(isUniqueFast("abcabc"))
