class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapped={ ")":"(" , "]":"[" , "}":"{" }
        for c in s:
            if c in mapped:
                if stack and stack[-1]==mapped[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False