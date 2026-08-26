class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for chara in s:
            if chara in "[({":
                stack.append(chara)

            else:
                if not stack:
                    return False

                if ((stack[-1] == '(' and chara == ')') or
                    (stack[-1] == '{' and chara == '}') or
                    (stack[-1] == '[' and chara == ']')):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0