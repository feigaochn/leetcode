class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """

        class Term:
            def __init__(self, coeff=0, vars=None):
                if vars is None:
                    vars = {'': 0}
                self.coeff = coeff
                self.vars = vars

            def __add__(self, other):
                if self.vars == other.vars:
                    coeff = self.coeff + other.coeff
                    if coeff == 0:
                        return Expr([Term()])
                    else:
                        return Expr([Term(coeff, self.vars)])
                else:
                    return Expr([
                        Term(self.coeff, self.vars),
                        Term(other.coeff, other.vars)
                    ])

            def __sub__(self, other):
                if self.vars == other.vars:
                    coeff = self.coeff - other.coeff
                    if coeff == 0:
                        return Expr([Term()])
                    else:
                        return Expr([Term(coeff, self.vars)])
                else:
                    return Expr([
                        Term(self.coeff, self.vars),
                        Term(-other.coeff, other.vars)
                    ])

            def __mul__(self, other):
                vars = self.vars.copy()
                for var, val in other.vars.items():
                    vars[var] = val + vars.get(var, 0)
                return Expr([Term(self.coeff * other.coeff, vars)])

            def __str__(self):
                result = str(self.coeff)
                if result != '0' and self.degree:
                    result += "*" + "*".join(self.vars_tuple)
                return result

            def __repr__(self):
                return str(self)

            @property
            def degree(self):
                return sum(self.vars.values())

            @property
            def vars_tuple(self):
                vars = []
                for var, val in self.vars.items():
                    vars.extend([var] * val)
                return tuple(sorted(vars))

            def __eq__(self, other):
                return self.coeff == other.coeff and self.vars == other.vars

        class Expr:
            def __init__(self, expr=None):
                self.expr = expr[:] if expr else [Term(0)]  # type: List[Term]

            def simplify(self):
                expr = []
                for term in sorted(
                        self.expr,
                        key=lambda t: (-t.degree, t.vars_tuple)):
                    if not expr:
                        expr.append(term)
                    else:
                        last = expr[-1]
                        if last.vars_tuple == term.vars_tuple:
                            expr.pop()
                            coeff = last.coeff + term.coeff
                            if coeff != 0:
                                expr.append(Term(coeff, term.vars))
                        else:
                            expr.append(term)
                self.expr = expr

            def __add__(self, other):
                result = Expr(self.expr + other.expr)
                result.simplify()
                return result

            def __sub__(self, other):
                result = Expr(self.expr +
                              [Term(-1 * t.coeff, t.vars) for t in other.expr])
                result.simplify()
                return result

            def __mul__(self, other):
                terms = [(t1 * t2).expr[0]
                         for t1 in self.expr for t2 in other.expr]
                result = Expr(terms)
                result.simplify()
                return result

            def to_list(self):
                self.simplify()
                return [str(term) for term in self.expr]

            def __repr__(self):
                return "Expr<{}>".format(self.to_list())

        import operator as op
        op_map = {'+': op.add, '-': op.sub, '*': op.mul}

        def eval_tokens(tokens):  # rtype: Expr
            stack = [[]]
            for token in tokens:
                if token == '(':
                    stack.append([])
                elif token == ')':
                    last_stack = stack.pop()
                    result = last_stack[0]
                    for opr, second in zip(last_stack[1::2], last_stack[2::2]):
                        result = opr(result, second)
                    stack[-1].append(result)
                elif token.isdigit():
                    stack[-1].append(Expr([Term(int(token))]))
                elif token.isalpha():
                    if token in knowns:
                        term = Term(knowns[token])
                    else:
                        term = Term(1, {token: 1})
                    stack[-1].append(Expr([term]))
                elif token in '+-*':
                    stack[-1].append(op_map[token])
                # print(token, stack)
                while len(stack[-1]) >= 3 and stack[-1][-2] == op.mul:
                    last = stack[-1].pop()
                    opr = stack[-1].pop()
                    first = stack[-1].pop()
                    stack[-1].append(opr(first, last))
            result = stack[-1][0]
            return result

        import re
        tokens = re.findall(r'\(|\)|\d+|\+|-|\w+|\*',
                            '( {} )'.format(expression))
        knowns = dict(zip(evalvars, evalints))
        # print(tokens, knowns)

        result = eval_tokens(tokens)
        # print(result)
        result = [x.strip('*') for x in result.to_list() if x != '0']

        return result


sol = Solution().basicCalculatorIV
print(sol(expression="e + 8 - a + 5", evalvars=["e"], evalints=[1]))
print(
    sol(expression="e - 8 + temperature - pressure",
        evalvars=["e", "temperature"],
        evalints=[1, 12]))
print(sol(expression="(e + 8) * (e - 8)", evalvars=[], evalints=[]))
print(sol(expression="7 - 7", evalvars=[], evalints=[]))
print(sol(expression="a * b * c + b * a * c * 4", evalvars=[], evalints=[]))
print(
    sol(expression=
        "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
        evalvars=[],
        evalints=[]))

print(sol("a * b * b", ["a"], [0]))
