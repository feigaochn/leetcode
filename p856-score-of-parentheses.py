# Given a balanced parentheses string S, compute the score of the string based
# on the following rule:
#     () has score 1
#     AB has score A + B, where A and B are balanced parentheses strings.
#     (A) has score 2 * A, where A is a balanced parentheses string.

# Example 1:
# Input: "()"
# Output: 1

# Example 2:
# Input: "(())"
# Output: 2

# Example 3:
# Input: "()()"
# Output: 2

# Example 4:
# Input: "(()(()))"
# Output: 6

# Note:
#     S is a balanced parentheses string, containing only ( and ).
#     2 <= S.length <= 50


class Solution:

    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for c in S:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack[-1] == "(":
                    stack[-1] = 1
                else:
                    stack[-2] = stack[-1] * 2
                    stack.pop()
            while (
                len(stack) >= 2
                and isinstance(stack[-1], int)
                and isinstance(stack[-2], int)
            ):
                stack[-2] += stack[-1]
                stack.pop()
        return stack[0]


sol = Solution().scoreOfParentheses
print(sol("()"), 1)
print(sol("(())"), 2)
print(sol("()()"), 2)
print(sol("(()(()))"), 6)
