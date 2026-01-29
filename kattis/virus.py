def popUntilFirstDifference(stack1, stack2):
    while (stack1 != [] and stack2 != []) and (stack1[-1] == stack2[-1]):
        stack1.pop()
        stack2.pop()

    return (stack1, stack2)


nonVirus = list(input())
virus = list(input())

nonVirus, virus = popUntilFirstDifference(nonVirus, virus)

nonVirus.reverse()
virus.reverse()

nonVirus, virus = popUntilFirstDifference(nonVirus, virus)

print(len(virus))