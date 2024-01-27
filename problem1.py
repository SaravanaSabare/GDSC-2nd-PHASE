def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            # Ignore characters other than parentheses
            return False

    return not stack

# Example usage with user input:
user_input = input("Enter a string with parentheses: ")
result = is_valid_parentheses(user_input)
print("Is the string valid?", result)
