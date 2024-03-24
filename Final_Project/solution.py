def is_valid(s: str) -> bool:
    stack = Stack()
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.push(char)
        elif char in mapping.keys():
            if stack.is_empty() or mapping[char] != stack.pop():
                return False
        else:
            return False

    return stack.is_empty()

# Example Usage:
print(is_valid("()[]{}"))  # Output: True
print(is_valid("([)]"))    # Output: False