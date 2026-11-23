class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack