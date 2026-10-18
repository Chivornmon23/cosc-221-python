def is_valid(str):
    stack = []

    matching = {')': '(', ']': '[', '}':'{'}

    for char in str:
        if char in matching.value():
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
        return len(stack) == 0