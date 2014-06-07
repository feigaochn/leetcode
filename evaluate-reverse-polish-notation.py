# author: Fei Gao
#
# Evaluate Reverse Polish Notation
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# Some examples:
# ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if not tokens:
            return None
        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: int(float(x) / y)}
        # note that python handle div differently!
        # py2, py3, and C/C++/Java may get all distinct results

        queue = list()
        for val in tokens:
            if isinstance(val, list):
                queue.append(self.evalRPN(val))
            elif val in op:
                o2 = queue.pop()
                o1 = queue.pop()
                queue.append(op[val](o1, o2))
            else:
                queue.append(int(val))
        return queue[-1]


def main():
    solver = Solution()
    tests = [["2", "1", "+", "3", "*"],
             ["4", "13", "5", "/", "+"],
             [["2", "1", "+", "3", "*"], "13", "5", "/", "+"],
             ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]]  # 22
    for test in tests:
        print(test)
        result = solver.evalRPN(test)
        print(' ->')
        print(result)
        print('~' * 10)
    pass


if __name__ == '__main__':
    main()
    pass
