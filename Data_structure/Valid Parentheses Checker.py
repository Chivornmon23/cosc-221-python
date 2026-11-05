def isValid(s: str) -> bool:
    bracketStack = []
    matchingPairs = { ')': '(','}':'{', ']':'[' }

    for currentChar in s: 
        if currentChar in matchingPairs.values(): 
            bracketStack.append(currentChar)
        elif currentChar in matchingPairs:
            if not bracketStack:
                return False
            topElement = bracketStack.pop()
            if topElement != matchingPairs[currentChar]:
                return False
        else: 
            return False
    return len(bracketStack) == 0


print(isValid("a{b(c[d]e)}"))