class Solution:
    def evaluate(self, expr):
        """
        :type expr: str
        :rtype: int
        """

        def match_paren(s: str):
            d = 1
            r = 0
            while d:
                r += 1
                if s[r] == ')':
                    d -= 1
                elif s[r] == '(':
                    d += 1
            return r

        def split(expr: str):
            expr = expr[1:-1]
            parts = []
            while expr:
                if expr[0] == '(':
                    rb = match_paren(expr)
                    first = expr[:rb + 1]
                    expr = expr[rb + 2:]
                else:
                    first, _, expr = expr.partition(' ')
                parts.append(first)
            return parts

        def eval(expr, local: dict = None):
            try:
                return int(expr)
            except ValueError:
                pass
            try:
                return local[expr]
            except (KeyError, TypeError):
                pass
            parts = split(expr)
            if parts[0] == 'add':
                return eval(parts[1], local) + eval(parts[2], local)
            elif parts[0] == 'mult':
                return eval(parts[1], local) * eval(parts[2], local)
            elif parts[0] == 'let':
                if local is None:
                    local = dict()
                local_update = local.copy()
                for v, e in zip(parts[1::2], parts[2::2]):
                    local_update[v] = eval(e, local_update)
                return eval(parts[-1], local_update)

        return eval(expr)


fn = Solution().evaluate

for expr in [
        "1",
        "12",
        "-1",
        "(add 12 32)",
        "(mult 22 44)",
        "(mult 22 (add 3 5))",
        "(mult 22 (add 3 (mult 3 5)))",
        "(let x 2 (add 3 x))",
        "(let x 2 x 3 (mult 3 x))",
        "(let x 1 y 2 x (add x y) (add x y))",
        "(let x 2 (add (let x 3 (let x 4 x)) x))",
        "(let a1 3 b2 (add a1 1) b2)",
        "(let x -2 y x y)",
]:
    print(expr, '->', fn(expr))
