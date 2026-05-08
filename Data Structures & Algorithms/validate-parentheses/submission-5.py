class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedMap = {')': '(', '}':'{', ']': '['}
       
        for bracket in s:
            if bracket in closedMap:
                if stack and stack[-1] == closedMap[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return True if not stack else False
            


        