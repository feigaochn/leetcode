# coding: utf-8

# author: Fei Gao
#
# Different Ways To Add Parentheses

# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
# Example 1
# Input: "2-1-1". 
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
# Example 2
# Input: "2*3-4*5" 
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10] 
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.
# Subscribe to see which companies asked this question


class Solution(object):
    def diffWaysToCompute(self, expr):
        """
        :type expr: str
        :rtype: List[int]
        """
        import operator
        ops = {'+': operator.add,
               '-': operator.sub,
               '*': operator.mul}

        def guess(expr):
            """guess possible results from input string
            :type expr: str
            :rtype: List[int]
            """
            results = []
            try:
                results.append(int(expr))
                return results
            except ValueError:
                pass
            for idx, ch in enumerate(expr):
                if ch in ops:
                    results.extend(ops[ch](l, r) for l in guess(expr[:idx]) for r in guess(expr[idx+1:]))
            return results

        return guess(expr)

def main():
    solver = Solution()
    tests = [
        ("2-1-1",),  # [0, 2]
        ("2*3-4*5",) # [-34, -14, -10, -10, 10]
    ]
    for test in tests:
        print(test)
        print(' ->')
        result = solver.diffWaysToCompute(*test)
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
